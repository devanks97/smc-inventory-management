from django.contrib import admin

# Register your models here.
from .models import record

from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportMixin

from import_export import resources

class ImportExportModelAdmin(ImportExportMixin, SimpleHistoryAdmin):
    """
    Subclass of ModelAdmin And SimpleHistoryAdmin with import/export functionality.
    """


class RecordResource(resources.ModelResource):

    class Meta:
        model = record
        exclude = ('id', )


class recordAdmin(ImportExportModelAdmin):
    #resource_class = RecordResource
    list_display = ['name', 'department', 'year', 'device']
    list_filter = ('department', 'year', 'device')
    pass

admin.site.register(record,recordAdmin)
