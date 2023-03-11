from rest_framework import serializers
from .models import ConcentrateQuality, ReportDate


class ConcentrateQualitySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ConcentrateQuality
        fields = [
            'user', 'time_create', 'material_name',
            'ferrum', 'silicium', 'aluminum',
            'calcium', 'sulfur', ]


class ReportDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportDate
        fields = "__all__"
