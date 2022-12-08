from rest_framework import viewsets

from .models import CategoryModel
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
