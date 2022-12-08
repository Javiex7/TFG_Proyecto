from rest_framework import serializers

from categories.models import CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'title',
            'content',
            'active'
        ]
