from django.db import models
from simple_history.models import HistoricalRecords
from .deviceListModel import deviceList

from ..modelFiles.CustomCharField import *
from ..modelFiles.CustomValidators import *
from django.core.validators import MinValueValidator

class record(models.Model):
    name = TitleCaseCharField(max_length=200,validators=[validate_correct_text])
    department = UpperCaseCharField(max_length=50,validators=[validate_correct_text])
    location = TitleCaseCharField(max_length=50,validators=[validate_correct_text])
    year = models.DecimalField(max_digits=4,decimal_places=0,validators=[MinValueValidator(2016)])
    device = models.ForeignKey(deviceList,on_delete=models.CASCADE)
    deviceTag = UpperCaseCharField(max_length=50,validators=[validate_deviceTag],unique=True)
    def __str__(self):
        return self.name
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Record Of Inventory'
        verbose_name_plural = 'Records Of Inventory'

import re
deviceTagPattern = re.compile("^([a-zA-z])(-)((?:[a-zA-Z][a-zA-Z]+))(-)((?:[a-zA-Z][a-zA-Z]+))(-)(\d+)$")

def validate_deviceTag_pre_save(sender, instance, **kwargs):
    instanceDeviceTag = instance.deviceTag
    if not deviceTagPattern.match(instanceDeviceTag):
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'DeviceTag "{}" is not following the format required'.format(instanceDeviceTag),code='deleting_protected')

models.signals.pre_save.connect(validate_deviceTag_pre_save, sender=record)
