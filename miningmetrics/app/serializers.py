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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['time_create'] = instance.time_create.strftime('%Y-%m-%d %H:%M:%S')
        return representation


# class ConcentrateStatisticSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConcentrateQuality
#         fields = [
#             'ferrum', 'silicium', 'aluminum',
#             'calcium', 'sulfur',
#         ]


class ReportDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportDate
        fields = "__all__"
