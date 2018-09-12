from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
