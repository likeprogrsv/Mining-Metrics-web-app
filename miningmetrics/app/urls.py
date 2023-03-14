from django.urls import include, path
from .views import ConcentrateQualityAPIList, ReportView, index

urlpatterns = [
    path('', index, name='home'),
    path('report/', ReportView.as_view(
        template_name='app/report.html'), name='report'
    ),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/report/<int:pk>/', ConcentrateQualityAPIList.as_view()),
]
