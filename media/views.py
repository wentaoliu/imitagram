from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from django.core.files.storage import FileSystemStorage
from media.models import Media


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