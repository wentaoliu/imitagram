from django.db import models
from django.contrib.auth.models import User


class Media(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

