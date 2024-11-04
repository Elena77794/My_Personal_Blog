import io
from datetime import date

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"



# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     body = serializers.CharField(max_length=1000)
#     author = serializers.CharField(max_length=255)
#     img_url = serializers.CharField(max_length=255)
#     subtitle = serializers.CharField(max_length=500)
#     date = serializers.DateField(read_only=True)
#     updated_at = serializers.DateField(read_only=True)
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.body = validated_data.get("body", instance.body)
#         instance.author = validated_data.get("author", instance.author)
#         instance.img_url = validated_data.get("img_url", instance.img_url)
#         instance.subtitle = validated_data.get("subtitle", instance.subtitle)
#         instance.date = validated_data.get("date", instance.date)
#         instance.updated_at = validated_data.get("updated_at", instance.updated_at)
#         instance.save()
#         return instance
#
