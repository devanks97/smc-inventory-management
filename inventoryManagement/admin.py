from django.contrib import admin
from django.db.models import Count

# Register your models here.
from .models import record
from .models import recordSummary

from import_export import resources

from .ModuleAdminSettings import ImportExportActionModelAdmin
# from .ModuleSummaryAdminSettings import recordSummaryAdmin

class RecordResource(resources.ModelResource):

    class Meta:
        model = record
        exclude = ('id', )
class recordSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/record_summary_change_list.html'
    list_display = ['department', 'device']
    list_filter = (
        'device','department','year'
    )
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
        request,
        extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
	
        response.context_data['summary'] = list(
        qs
        .values('department','device')
        .annotate(total=Count('id'))
        .order_by('total')
        )
        return response
        
class recordAdmin(ImportExportActionModelAdmin):
    #resource_class = RecordResource
    list_display = ['name', 'department', 'year', 'device']
    list_filter = ('department', 'year', 'device')
    search_fields = ('name', 'department')
    pass

admin.site.register(record,recordAdmin)
admin.site.register(recordSummary,recordSummaryAdmin)