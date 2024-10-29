from django.http import HttpResponse
from django.shortcuts import render

import requests


# Create your views here.
def home(request):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    data = {"posts": response
            }
    return render(request, "posts/index.html", data)


def show_post(request, post_id):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    for item in response:
        if item["id"] == post_id:
            data = {"body": item["body"],
                    "title": item["title"],
                    "subtitle": item["subtitle"]}
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
        return  HttpResponse("Succesfully sent your message")
    return render(request, "posts/contact.html")
