from django.contrib import admin

# Register your models here.
from .models import record

from simple_history.admin import SimpleHistoryAdmin

'''
#from import_export import resources

#from import_export.admin import ImportExportModelAdmin



class RecordResource(resources.ModelResource):

    class Meta:
        model = record
        exclude = ('id', )
'''

class recordAdmin(SimpleHistoryAdmin):
    list_display = ['name', 'department', 'year', 'device']
    list_filter = ('department', 'year', 'device')
    history_list_display = ["status"]
    pass

admin.site.register(record,recordAdmin)
