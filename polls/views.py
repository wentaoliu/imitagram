from polls.models import Question
from polls.serializers import QuestionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class QustionList(APIView):

    permission_classes = (IsAuthenticated,)

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        questions = Question.objects.all()
        print(request.user.username)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)