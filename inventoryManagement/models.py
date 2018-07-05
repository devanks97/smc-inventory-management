from django.db import models
from simple_history.models import HistoricalRecords

from django.core.validators import MinValueValidator,RegexValidator

class UpperCaseCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)

validate_correct_text = RegexValidator(regex='^([a-zA-Z0-9]+\s)*[a-zA-Z0-9]+$',message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.',code='invalid_text')

validate_deviceTag = RegexValidator(regex='^([a-zA-z])(-)((?:[a-zA-Z][a-zA-Z]+))(-)((?:[a-zA-Z][a-zA-Z]+))(-)(\d+)$',message='The device tag MUST follow the pattern <location_firstLetter>-<department>-<deviceShortName>-<intergerNumber>',code='invalid_deviceTag')


class deviceList(models.Model):
    deviceName = models.CharField(primary_key=True,max_length=50,validators=[validate_correct_text])
    def __str__(self):
        return self.deviceName
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'List Of Devices'


class record(models.Model):
    name = models.CharField(max_length=200,validators=[validate_correct_text],unique=True)
    department = models.CharField(max_length=50,validators=[validate_correct_text])
    location = models.CharField(max_length=50,validators=[validate_correct_text])
    year = models.DecimalField(max_digits=4,decimal_places=0,validators=[MinValueValidator(2016)])
    device = models.ForeignKey(deviceList,on_delete=models.CASCADE)
    deviceTag = models.UpperCaseCharField(max_length=50,validators=[validate_deviceTag])
    def __str__(self):
        return self.name
    def department_list(self):
        return self.department
    def year_list(self):
        return self.year
    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Record Of Inventory'
        verbose_name_plural = 'Records Of Inventory'
class recordSummary(record):
    class Meta:
	        proxy = True
	        verbose_name = 'Department Inventory'
	        verbose_name_plural = 'Departments Inventory'