from django import forms
from ckeditor.fields import RichTextFormField
from .models import Post
from django.contrib.auth.models import User


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'author', 'img_url', 'body']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
