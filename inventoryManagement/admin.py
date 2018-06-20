from django.contrib import admin
from django.db.models import Count

# Register your models here.
from .models import record
from .models import recordSummary

from import_export import resources

from .adminFiles.ModuleExportActionModelAdminSettings import ImportExportActionModelAdmin
from .adminFiles.ModuleSummaryAdminSettings import recordSummaryAdmin
from .adminFiles.ModuleCachingPaginatorSettings import CachingPaginator

class RecordResource(resources.ModelResource):

    class Meta:
        model = record
        exclude = ('id', )
       
class recordAdmin(ImportExportActionModelAdmin):
    #resource_class = RecordResource
    list_display = ['name', 'department', 'year', 'device']
    list_filter = ('department', 'year', 'device')
    search_fields = ('name', 'department')
    show_full_result_count = False
    paginator = CachingPaginator
    pass

admin.site.register(record,recordAdmin)
admin.site.register(recordSummary,recordSummaryAdmin)