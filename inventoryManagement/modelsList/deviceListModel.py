from django.db import models

from .modelFiles.CustomCharField import *
from .modelFiles.CustomValidators import *

class deviceList(models.Model):
    deviceName = TitleCaseCharField(primary_key=True,max_length=50,validators=[validate_correct_text])
    def __str__(self):
        return self.deviceName
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'List Of Devices'