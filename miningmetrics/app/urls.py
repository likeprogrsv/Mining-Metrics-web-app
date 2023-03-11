from re import template
from django.urls import path
from .views import ConcentrateQualityAPIList, ReportView

urlpatterns = [
    path('report/', ReportView.as_view(template_name='app/report.html')),
    path('api/v1/report/<int:pk>/', ConcentrateQualityAPIList.as_view()),
]
