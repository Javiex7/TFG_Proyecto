from rest_framework import serializers

from categories.models import CategoryModel, DocumentFileModel, PointPackModel, CustomImageModel
from activities.models import QuizModel
from profiles.models import Profile

from activities.serializers import ShortQuizSerializer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFileModel
        fields = [
            'id',
            'name',
            'file'
        ]


class CustomImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(
        'get_image_url', read_only=True)

    class Meta:
        model = CustomImageModel
        fields = [
            'name',
            'image'
        ]

    def get_image_url(self, image):
        request = self.context.get('request')
        image_url = image.image.url
        return request.build_absolute_uri(image_url)


class PointPackDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(
        'get_pack_images', read_only=True)

    purchased = serializers.SerializerMethodField(
        'get_purchased_status', read_only=True)

    class Meta:
        model = PointPackModel
        fields = [
            'id',
            'name',
            'price',
            'images',
            'purchased'
        ]

    def get_pack_images(self, pack):
        request = self.context.get('request')
        serializer = CustomImageSerializer(
            instance=pack.images, many=True, context={"request": request})
        return serializer.data

    def get_purchased_status(self, pack):
        profile = Profile.objects.get(user__id=self.context['request'].user.id)
        if (profile and profile.purchased_packs):
            if profile.purchased_packs.filter(id=pack.id).exists():
                return True

        return False


class PointPackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointPackModel
        fields = [
            'id',
            'name'
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

    associated_packs = serializers.SerializerMethodField(
        'get_associated_point_packs', read_only=True)

    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'title',
            'content',
            'image',
            'quizzes',
            'associated_files',
            'associated_packs'
        ]

    def get_category_quizzes(self, category_detail):
        category_quizzes = QuizModel.objects.filter(
            category__id=category_detail.id, active=True)

        return ShortQuizSerializer(category_quizzes, many=True).data

    def get_associated_files(self, category_detail):
        return FileSerializer(category_detail.files, many=True).data

    def get_associated_point_packs(self, category_detail):
        return PointPackListSerializer(category_detail.packs, many=True).data
