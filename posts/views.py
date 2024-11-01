from django.contrib.auth import login, authenticate
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegistrationForm, UserLoginForm
import requests

from .forms import CreatePostForm
from .models import BlogPost



def home(request):
    posts = BlogPost.objects.all()
    data = {"posts": posts
            }
    return render(request, "posts/index.html", data)


def show_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    data = {'post': post}
    return render(request, "posts/post.html", data)


def about_page(request):
    return render(request, "posts/about.html")


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Come from {name}, mail_box {email}, phone_number: {phone_number} with message {message}")
        return HttpResponse("Succesfully sent your message")
    return render(request, "posts/contact.html")


def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, "posts/make-post.html", {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        edit_form = CreatePostForm(request.POST, instance=post)
        if edit_form.is_valid():
            edit_form.save()  # Save the updated post
            return redirect('post', post_id=post.id)
    else:
        edit_form = CreatePostForm(instance=post)
    data = {"form": edit_form}
    return render(request, "posts/make-post.html", data)


def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, "posts/index.html")


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'posts/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'posts/login.html', {'form': form})






