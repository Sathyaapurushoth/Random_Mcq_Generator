#from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Mcqs, Question
from .serializers import McqSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView

class Mcq(generics.ListAPIView):

    serializer_class = McqSerializer
    queryset = Mcqs.objects.all()

    
class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(mcq__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class McqQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(mcq__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
