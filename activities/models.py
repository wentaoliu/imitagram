from django.db import models
from media.models import Like
from django.contrib.auth.models import User
from relationships.models import Relationship
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from media.models import Media

# Create your models here.
class Activity(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='actor')
    target = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='target')
    verb = models.CharField(max_length=50)
    obj = models.ForeignKey(Media, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Relationship)
def follow_post_save(sender, **kwargs):
    relationship = kwargs['instance']
    activity = Activity()
    activity.actor = relationship.source
    activity.target = relationship.sink
    activity.verb = 'follow'
    activity.save()


@receiver(post_save, sender=Like)
def like_post_save(sender, **kwargs):
    like = kwargs['instance']
    activity = Activity()
    activity.actor = like.user
    activity.target = like.media.uploader
    activity.verb = 'like'
    activity.obj = like.media
    activity.save()