from .models import record
from .models import recordSummary
from .models import deviceList

from .adminFiles.ModuleRecordAdmin import recordAdmin
from .adminFiles.ModuleSummaryAdmin import recordSummaryAdmin
from .adminFiles.ModuleDeviceListAdmin import deviceListAdmin

admin.site.register(deviceList,deviceListAdmin)
admin.site.register(record,recordAdmin)
admin.site.register(recordSummary,recordSummaryAdmin)
