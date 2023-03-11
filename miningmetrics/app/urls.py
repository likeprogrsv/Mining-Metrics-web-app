from re import template
from django.urls import path
from .views import ConcentrateQualityAPIList, ReportView

urlpatterns = [
    path('report/<int:pk>', ReportView.as_view(template_name='app/report.html')),
    path('api/v1/report/', ConcentrateQualityAPIList.as_view()),
]
