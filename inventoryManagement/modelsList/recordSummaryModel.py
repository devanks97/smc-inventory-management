from django.db import models

from .recordModel import record

class recordSummary(record):
    class Meta:
	        proxy = True
	        verbose_name = 'Department Grouped Graph'
	        verbose_name_plural = 'Departments Grouped Graph'