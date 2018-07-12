from .ModuleExportActionModelAdmin import ImportExportActionModelAdmin
from .ModuleRecordResource import RecordResource
from .ModuleCachingPaginator import CachingPaginator

class recordAdmin(ImportExportActionModelAdmin):
    resource_class = RecordResource
    list_display = ['name', 'department', 'year', 'device','deviceTag','building','old_device_tag','item_description','serial_no','brand','model_no','service_tag','floor','room','remarks']
    list_filter = ('department', 'year', 'device')
    search_fields = ('name', 'department','deviceTag','old_device_tag')
    show_full_result_count = False
    paginator = CachingPaginator
    pass
