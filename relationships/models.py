from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Relationship(models.Model):
    source = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='source')
    sink = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sink')
    created_at = models.DateTimeField(auto_now_add=True)
