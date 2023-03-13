from re import L
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ConcentrateQuality, ReportDate
from .serializers import ConcentrateQualitySerializer
from django.views.generic import TemplateView, DetailView, ListView


class ConcentrateQualityAPIList(generics.ListCreateAPIView):
    lookup_field = 'pk'
    # queryset = ConcentrateQuality.objects.all()
    serializer_class = ConcentrateQualitySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        report_date_id = self.kwargs['pk']
        return ConcentrateQuality.objects.filter(
            report_month_id=report_date_id
        )

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)

        for obj in serializer.validated_data:
            ConcentrateQuality.objects.get_or_create(**obj)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReportView(ListView):
    model = ReportDate
