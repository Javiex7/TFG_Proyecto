from rest_framework import viewsets

from .models import CategoryModel
from .serializers import CategoryListSerializer, CategoryDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = CategoryModel.objects.filter(active=True)
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategoryDetailSerializer
