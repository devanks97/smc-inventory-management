from django.contrib import admin
from django.db.models import Count

# Register your models here.
from .models import record
from .models import recordSummary
from .models import deviceList

from import_export import resources

from .adminFiles.ModuleExportActionModelAdminSettings import ImportExportActionModelAdmin
from .adminFiles.ModuleSummaryAdminSettings import recordSummaryAdmin
from .adminFiles.ModuleCachingPaginatorSettings import CachingPaginator

class RecordResource(resources.ModelResource):

    class Meta:
        model = record
        # fields = ('name','department','location','year','device__deviceName')
        exclude = ('id', )
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped = True

class deviceListResource(resources.ModelResource):

    class Meta:
        model = deviceList
        # fields = ('name','department','location','year','device__deviceName')
        exclude = ('id', )
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped = True

class deviceListAdmin(admin.ModelAdmin):
    list_display = ['deviceName']
    show_full_result_count = False
    paginator = CachingPaginator
    pass
		
class recordAdmin(ImportExportActionModelAdmin):
    resource_class = RecordResource
    list_display = ['name', 'department', 'year', 'device', 'location']
    list_filter = ('department', 'year', 'device')
    search_fields = ('name', 'department')
    show_full_result_count = False
    paginator = CachingPaginator
    pass

admin.site.register(deviceList,deviceListAdmin)
admin.site.register(record,recordAdmin)
admin.site.register(recordSummary,recordSummaryAdmin)