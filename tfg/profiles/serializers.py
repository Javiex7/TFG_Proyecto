from rest_framework import serializers
from django.contrib.auth.models import User

from profiles.models import Profile
from categories.serializers import PointPackListSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True, many=False)

    class Meta:
        model = Profile
        fields = [
            'user',
            'points',
            'obtained_points'
        ]


class DetailedProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True, many=False)
    purchased_packs = PointPackListSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = [
            'user',
            'group',
            'points',
            'obtained_points',
            'purchased_packs'
        ]
