from rest_framework import serializers

from activities.models import ActivityModel


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        fields = [
            'id',
            'title',
            'type',
            'category',
            'active'
        ]
