from django import forms
from ckeditor.fields import RichTextFormField  # Import CKEditor form field
from .models import BlogPost


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'author', 'img_url', 'body']

    body = RichTextFormField()  # Assign CKEditor to the 'body' field