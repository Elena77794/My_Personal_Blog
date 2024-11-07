from datetime import timezone
from django.contrib.auth.models import User

import self as self
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, FormView, DeleteView, CreateView
from django.forms import model_to_dict
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .forms import UserRegistrationForm, UserLoginForm
import requests

from .forms import CreatePostForm
from .models import Post
from rest_framework import generics, status, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PostSerializer


class PostAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10000


class PostAPIList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PostAPIListPagination

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'posts': PostSerializer(queryset, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_instance = request.user
        post_new = Post.objects.create(
            title=request.data["title"],
            body=request.data["author"],
            img_url=request.data["img_url"],
            subtitle=request.data["subtitle"],
            user=user_instance

        )
        return Response({"post": PostSerializer(post_new).data})


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"eroor": "Method PUT not allowed"})

        try:
            instance = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Object does not exists"})

        serializer = PostSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class PostApiDestroy(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"}, status=404)

        serializer = PostSerializer(instance)
        return Response(serializer.data, status=200)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = PostSerializer(instance)
        response_data = {
            "message": "This post will be deleted",
            "post": serializer.data
        }
        instance.delete()
        return Response(response_data, status=204)


class BlogHome(ListView):
    model = Post
    template_name = "posts/index.html"


class ShowPost(DetailView):
    model = Post
    template_name = "posts/post.html"


class CreatePost(FormView):
    form_class = CreatePostForm
    template_name = "posts/make_post.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)


class EditPost(UpdateView):
    model = Post
    fields = ['title', 'body', 'img_url', 'subtitle']
    template_name = "posts/make_post.html"
    success_url = reverse_lazy('post')

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("home")


class RegisterUser(FormView):
    form_class = UserRegistrationForm
    template_name = 'posts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginUser(FormView):
    form_class = UserLoginForm
    template_name = 'posts/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Come from {name}, mail_box {email}, phone_number: {phone_number} with message {message}")
        return HttpResponse("Succesfully sent your message")
    return render(request, "posts/contact.html")


def about_page(request):
    return render(request, "posts/about.html")
