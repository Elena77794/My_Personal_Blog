from django import forms
from ckeditor.fields import RichTextFormField  # Import CKEditor form field
from .models import BlogPost
from django.contrib.auth.models import User


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'author', 'img_url', 'body']

    body = RichTextFormField()  # Assign CKEditor to the 'body' field


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
