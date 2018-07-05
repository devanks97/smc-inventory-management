from ..models import record
from import_export import resources

class RecordResource(resources.ModelResource):

    class Meta:
        model = record
        exclude = ('id', )
        import_id_fields = ('deviceTag',)
        skip_unchanged = True
        report_skipped = True