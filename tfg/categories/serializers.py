from rest_framework import serializers

from categories.models import CategoryModel
from categories.models import DocumentFileModel
from activities.models import QuizModel

from activities.serializers import QuizSerializer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFileModel
        fields = [
            'id',
            'name',
            'file'
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'title',
            'short_description',
            'image'
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    quizzes = serializers.SerializerMethodField(
        'get_category_quizzes', read_only=True)

    associated_files = serializers.SerializerMethodField(
        'get_associated_files', read_only=True)

    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'title',
            'content',
            'image',
            'quizzes',
            'associated_files'
        ]

    def get_category_quizzes(self, category_detail):
        category_quizzes = QuizModel.objects.filter(
            category__id=category_detail.id)

        return QuizSerializer(category_quizzes, many=True).data

    def get_associated_files(self, category_detail):
        return FileSerializer(category_detail.files, many=True).data
