from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
       Represents a blog post in the application.

       Fields:
           - title: The main title of the blog post.
           - subtitle: A subtitle providing additional context.
           - body: The main content of the post.
           - img_url: URL to an image associated with the post.
           - author: Name of the author.
           - user: Reference to the user who created the post.
           - date: Date the post was created.
           - updated_at: Date the post was last updated.
       """
    title = models.CharField(max_length=100, verbose_name="Title")
    date = models.DateField(auto_now_add=True, verbose_name="Date Created")
    updated_at = models.DateField(auto_now=True, verbose_name="Last Updated")
    body = models.TextField(max_length=1000, verbose_name="Content")
    author = models.CharField(max_length=255, verbose_name="Author")
    img_url = models.CharField(max_length=255, verbose_name="Image Url")
    subtitle = models.CharField(max_length=500, verbose_name="Subtitle")
    user = models.ForeignKey(User,  verbose_name="Users", on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_post'
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
