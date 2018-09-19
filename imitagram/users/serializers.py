from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'profile_picture')


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'profile_picture', 'bio', 'website', 'is_business')

