from django.contrib.auth import login
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegistrationForm
import requests

from .forms import CreatePostForm
from .models import BlogPost


# Create your views here.
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
        edit_form = CreatePostForm(request.POST, instance=post)  # Populate the form with post data
        if edit_form.is_valid():
            edit_form.save()  # Save the updated post
            return redirect('post', post_id=post.id)
    else:
        edit_form = CreatePostForm(instance=post)  # Pre-fill the form with current post data
    data = {"form": edit_form}
    return render(request, "posts/make-post.html", data)


def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id) # Retrieve the post to be deleted
    if request.method == "POST":  # Ensure it's a POST request                        # Ensure this block runs in a transaction
        post.delete()  # Delete the post
        return redirect('home')  # Redirect to a suitable page after deletion
    return render(request, "posts/index.html")


def register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user instance but don't save to DB yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Now save the user to the database

            # Automatically log in the user after registration
            login(request, user)
            return redirect('home')  # Change 'home' to your home page
    else:
        form = UserRegistrationForm()
    return render(request, 'posts/register.html', {'form': form})


