from django.http import HttpResponse
from django.shortcuts import render

import requests


#Create your views here.
def home(request):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    data = { "posts": response
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
    return render(request, "posts/contact.html")