from django.db import models
from simple_history.models import HistoricalRecords

from django.core.validators import MinValueValidator

class record(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    year = models.DecimalField(max_digits=4,decimal_places=0,validators=[MinValueValidator(2016)])
    pc = 'pc'
    lt = 'lt'
    DEVICE_CHOICES = (
        (pc, 'Personal Computer'),
        (lt, 'Laptop'),
    )
    device = models.CharField(
        max_length=2,
        choices=DEVICE_CHOICES,
        default=pc,
    )
    def __str__(self):
        return self.name
    def department_list(self):
        return self.department
    def year_list(self):
        return self.year
    def device_list(self):
        return self.device
    history = HistoricalRecords()