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
from activities.models import Activity
from activities.serializer import ActivitySerializer
from relationships.models import Relationship


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def following(request):
    following = [x.sink for x in Relationship.objects.filter(source=request.user)]
    activities = Activity.objects.order_by('-created_at').filter(actor__in=following)[:10]
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def self(request):
    activities = Activity.objects.order_by('-created_at').filter(target=request.user)[:10]
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)
