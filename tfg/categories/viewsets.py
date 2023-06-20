from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from profiles.models import Profile
from .models import CategoryModel, PointPackModel
from .serializers import CategoryListSerializer, CategoryDetailSerializer, PointPackDetailSerializer, PointPackListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CategoryModel.objects.filter(
        active=True, generic=False).order_by("order")
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategoryDetailSerializer


class PointPackViewSet(GenericViewSet, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = PointPackModel.objects.filter(active=True)
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'list':
            return PointPackListSerializer
        if self.action == 'retrieve':
            return PointPackDetailSerializer
        return PointPackDetailSerializer

    @action(detail=True, methods=['get'])
    def buyPointPack(self, request, *args, **kwargs):
        # Check the existence of the pack and if it has been bought
        pack_id = kwargs.get('pk')
        packs = PointPackModel.objects.filter(id=pack_id)

        if not packs:
            return Response("Pack with id: '" + pack_id + "' not found", status.HTTP_404_NOT_FOUND)

        pack = packs.first()
        profile = Profile.objects.get(user__id=request.user.id)

        if (profile and profile.purchased_packs):
            # Already bought pack
            if profile.purchased_packs.filter(id=pack.id).exists():
                serializer = self.get_serializer(pack)
                return Response(serializer.data, status.HTTP_204_NO_CONTENT)

        # Try to buy the pack
        if (pack.price > profile.points):
            return Response("Not enough points to buy the pack. Price: " + str(pack.price) + ", Actual points: " + str(profile.points),
                            status.HTTP_404_NOT_FOUND)

        profile.points -= pack.price
        profile.purchased_packs.add(pack)
        profile.save()

        # Return the pack
        serializer = PointPackDetailSerializer(
            instance=pack, context={"request": request})
        return Response(serializer.data, status.HTTP_200_OK)
