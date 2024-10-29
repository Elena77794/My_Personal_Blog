from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.show_post, name="post"),
    path('about/', views.about_page, name="about"),
    path('contact/', views.contact_page, name="contact")
]

