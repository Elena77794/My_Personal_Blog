from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.show_post, name="post"),
    path('about/', views.about_page, name="about"),
    path('contact/', views.contact_page, name="contact"),
    path('new-post/', views.create_post, name="new_post"),
    path('edit-post/<int:post_id>', views.edit_post, name="edit_post"),
    path('delete-post/<int:post_id>', views.delete_post, name="delete_post"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login")
]

