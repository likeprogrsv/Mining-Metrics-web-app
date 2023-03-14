from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ConcentrateQuality, ReportDate
from .serializers import ConcentrateQualitySerializer
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ConcentrateQualityAPIList(generics.ListCreateAPIView):
    lookup_field = 'pk'
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def index(request):
    return render(request, 'app/index.html')
