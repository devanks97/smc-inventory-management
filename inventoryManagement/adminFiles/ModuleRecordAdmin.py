from .ModuleExportActionModelAdmin import ImportExportActionModelAdmin
from .ModuleRecordResource import RecordResource
from .ModuleCachingPaginator import CachingPaginator

class recordAdmin(ImportExportActionModelAdmin):
    resource_class = RecordResource
    list_display = ['name', 'department', 'year', 'device', 'location','deviceTag']
    list_filter = ('department', 'year', 'device')
    search_fields = ('name', 'department','deviceTag')
    show_full_result_count = False
    paginator = CachingPaginator
    pass
