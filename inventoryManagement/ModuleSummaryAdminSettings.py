from django.contrib import admin
from django.db.models import Count

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
    # def get_queryset(self, request):
        # qs = super(recordSummaryAdmin, self).get_queryset(request)
        # return qs.values('department','device').annotate(total=Count('id')).order_by('total')