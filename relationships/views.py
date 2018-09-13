from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes, parser_classes
from relationships.models import Relationship


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def follow(request):
    edge = Relationship()
    edge.source = request.user
    edge.sink = User.objects.get(pk=request.data['follow'])
    edge.save()
    return Response(status=204)
