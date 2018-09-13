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
from media.models import Media
from media.serializers import MediaSerializer
from relationships.models import Relationship


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self_media_recent(request):
    posts = Media.objects.filter(uploader=request.user).order_by('-created_at')[:10]
    serializer = MediaSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self_suggest(request):
    following = Relationship.objects.filter(source=request.user)[:5]
    # TODO
    suggests = []
    for f in following:
        suggests.append(Relationship.objects.get(source=f.sink).sink)
    serializer = UserSerializer(suggests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def search(request):
    query = request.query_params['q']
    users = User.objects.filter(username__icontains=query)[:10]
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self_feed(request):
    following = [x.sink for x in Relationship.objects.filter(source=request.user)]
    posts = Media.objects.order_by('-created_at').filter(uploader_id__in=following)[:10]
    serializer = MediaSerializer(posts, many=True)
    return Response(serializer.data)