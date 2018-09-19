from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from imitagram.media.models import Media
from imitagram.media.serializers import MediaSerializer
from imitagram.relationships.models import Relationship
from .serializers import UserSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self_media_recent(request):
    posts = Media.objects.filter(user=request.user).order_by('-created_time')[:10]
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