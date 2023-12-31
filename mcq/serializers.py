from rest_framework import serializers
from .models import Mcqs, Question, Answer


class McqSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mcqs
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):


    class Meta:
    
        model = Question
        fields = [
            'title','answer',
        ]

        answer = AnswerSerializer(many=True, read_only=True)


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Question
        fields = [
            'mcq','title','answer',
        ]

        answer = AnswerSerializer(many=True, read_only=True)
        mcq = McqSerializer(read_only=True)
