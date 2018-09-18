from rest_framework import serializers
from django.contrib.auth.models import User
from activities.models import Activity
from media.models import Media
from media.serializers import MediaSerializer
from users.serializers import UserSerializer

class ActivitySerializer(serializers.ModelSerializer):
    actor = UserSerializer()
    target = UserSerializer()
    obj = MediaSerializer(required=False)
    class Meta:
        model = Activity
        fields = ('id', 'actor', 'target', 'verb', 'obj', 'created_at')