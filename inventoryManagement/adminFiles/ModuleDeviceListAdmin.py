from django.contrib import admin
from .ModuleCachingPaginator import CachingPaginator

class deviceListAdmin(admin.ModelAdmin):
    list_display = ['deviceName']
    show_full_result_count = False
    paginator = CachingPaginator
    pass