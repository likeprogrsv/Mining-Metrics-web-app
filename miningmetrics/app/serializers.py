from rest_framework import serializers
from .models import ConcentrateQuality, ReportDate


class ConcentrateQualitySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели с показателями концентрата"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    report_month = serializers.PrimaryKeyRelatedField(
        queryset=ReportDate.objects.all()
    )

    class Meta:
        model = ConcentrateQuality
        fields = [
            'user', 'time_create',
            'material_name', 'ferrum', 'silicium',
            'aluminum', 'calcium', 'sulfur', 'report_month'
        ]

    def to_representation(self, instance):
        """Форматируем дату и вермя для отображения в таблице"""
        representation = super().to_representation(instance)
        if 'time_create' in representation:
            representation['time_create'] = instance.time_create.strftime(
                '%Y-%m-%d %H:%M:%S'
            )
            return representation


class ReportDateSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели с датами отчетов"""
    class Meta:
        model = ReportDate
        fields = "__all__"
