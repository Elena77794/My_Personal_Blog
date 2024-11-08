from django.urls import path
from . import views
from posts.views import PostAPIList, UpdateBlogApi, DeletePostApi

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('post/<int:pk>', views.ShowPost.as_view(), name="post"),
    path('about/', views.about_page, name="about"),
    path('contact/', views.contact_page, name="contact"),
    path('new-post/', views.CreatePost.as_view(), name="new_post"),
    path('edit-post/<int:pk>', views.EditPost.as_view(), name="edit_post"),
    path('delete-post/<int:pk>', views.DeletePost.as_view(), name="delete_post"),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('api/v1/post/', PostAPIList.as_view()),
    path('api/v1/post/<int:pk>/', UpdateBlogApi.as_view()),
    path('api/v1/delete/<int:pk>/', DeletePostApi.as_view()),
]
