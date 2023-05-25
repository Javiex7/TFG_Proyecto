from rest_framework import serializers

from .models import QuizModel, QuestionModel, UserQuizModel


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = [
            'id',
            'question',
            'image',
            'option_a',
            'option_b',
            'option_c',
            'option_d'
        ]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = QuizModel
        fields = [
            'id',
            'name',
            'description',
            'category',
            'max_tries',
            'questions',
            'active'
        ]


class UserQuizSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = UserQuizModel
        fields = [
            'id',
            'quiz',
            'user',
            'tries',
            'correct_answers'
        ]


class UserQuizAnsweredSerializer(serializers.Serializer):
    correct_answers = serializers.IntegerField()
    points = serializers.IntegerField()
