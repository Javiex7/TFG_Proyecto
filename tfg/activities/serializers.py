from rest_framework import serializers

from .models import QuizModel


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = [
            'id',
            'name',
            'description',
            'category',
            'active'
        ]
