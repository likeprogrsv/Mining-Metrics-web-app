from re import L
from django.shortcuts import render
from rest_framework import generics
from .models import ConcentrateQuality, ReportDate
from .serializers import ConcentrateQualitySerializer
from django.views.generic import TemplateView, DetailView, ListView


class ConcentrateQualityAPIList(generics.ListCreateAPIView):
    lookup_field = 'pk'
    # queryset = ConcentrateQuality.objects.all()
    serializer_class = ConcentrateQualitySerializer

    def get_queryset(self):
        report_date_id = self.kwargs['pk']
        return ConcentrateQuality.objects.filter(
            report_month_id=report_date_id
        )



class ReportView(ListView):
    model = ReportDate
