from django.db import models
from simple_history.models import HistoricalRecords

from django.core.validators import MinValueValidator

from .modelFiles.CustomValidators import *

class deviceList(models.Model):
    deviceName = models.CharField(primary_key=True,max_length=50,validators=[validate_correct_text])
    def __str__(self):
        return self.deviceName
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'List Of Devices'

class record(models.Model):
    name = models.CharField(max_length=200,validators=[validate_correct_text])
    department = models.CharField(max_length=50,validators=[validate_correct_text])
    location = models.CharField(max_length=50,validators=[validate_correct_text])
    year = models.DecimalField(max_digits=4,decimal_places=0,validators=[MinValueValidator(2016)])
    device = models.ForeignKey(deviceList,on_delete=models.CASCADE)
    deviceTag = UpperCaseCharField(max_length=50,validators=[validate_deviceTag],unique=True)
    def __str__(self):
        return self.name
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Record Of Inventory'
        verbose_name_plural = 'Records Of Inventory'
		
class recordSummary(record):
    class Meta:
	        proxy = True
	        verbose_name = 'Department Inventory'
	        verbose_name_plural = 'Departments Inventory'