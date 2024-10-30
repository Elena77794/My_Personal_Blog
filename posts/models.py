# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from ckeditor.fields import RichTextField
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    body = models.TextField(max_length=1000)
    author = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500)
    body = RichTextField()

    class Meta:
        managed = False
        db_table = 'blog_post'



