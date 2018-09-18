from rest_framework import serializers
from django.contrib.auth.models import User
from imitagram.users.serializers import UserSerializer
from .models import Media, Comment


class MediaSerializer(serializers.ModelSerializer):
    uploader = UserSerializer()
    class Meta:
        model = Media
        fields = ('id', 'uploader', 'image_url','lat','lng','comments_count','likes_count','created_at')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'created_at')
        