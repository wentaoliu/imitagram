from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from django.core.files.storage import FileSystemStorage
from imitagram.users.serializers import UserSerializer
from .models import Media, Comment, Like
from .serializers import CommentSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@parser_classes((MultiPartParser, JSONParser, ))
def upload(request):
    file_obj = request.data['file']
    fs = FileSystemStorage()
    filename = fs.save(file_obj.name, file_obj)
    upload_file_url = fs.url(filename)
    m = Media(image_url = upload_file_url)
    m.uploader = request.user
    m.lat = request.data['lat']
    m.lng = request.data['lng']
    m.save()
    return Response(status=204)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def comments(request, id):
    if request.method == 'GET':
        data = Comment.objects.filter(media_id=id)
        serializer = CommentSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        media = Media.objects.get(pk=id)
        c = Comment(media=media)
        c.user = request.user
        c.text = request.data['text']
        c.save()
        # TODO
        # update cache counter
        return Response(status=204)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def likes(request, id):
    if request.method == 'GET':
        data = Like.objects.select_related('user').filter(media_id=id)
        likes = [x.user for x in data]
        serializer = UserSerializer(likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        media = Media.objects.get(pk=id)
        c = Like(media=media)
        c.user = request.user
        c.save()
        # TODO
        # update cache counter
        return Response(status=204)