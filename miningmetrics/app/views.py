from re import L
from django.shortcuts import render
from rest_framework import generics
from .models import ConcentrateQuality, ReportDate
from .serializers import ConcentrateQualitySerializer
from django.views.generic import TemplateView, DetailView, ListView


class ConcentrateQualityAPIList(generics.ListCreateAPIView):
    queryset = ConcentrateQuality.objects.all()
    serializer_class = ConcentrateQualitySerializer


class ReportView(ListView):
    model = ReportDate
    
    