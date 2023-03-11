from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class ReportDate(models.Model):
    class Meta:
        ordering = ['date']

    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)


class ConcentrateQuality(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    material_name = models.TextField(blank=False)

    ferrum = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0')),
                    MaxValueValidator(Decimal('100.0'))]
    )

    silicium = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0')),
                    MaxValueValidator(Decimal('100.0'))]
    )

    aluminum = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0')),
                    MaxValueValidator(Decimal('100.0'))]
    )

    calcium = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0')),
                    MaxValueValidator(Decimal('100.0'))]
    )

    sulfur = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0')),
                    MaxValueValidator(Decimal('100.0'))]
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    report_month = models.ForeignKey(ReportDate, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.material_name
