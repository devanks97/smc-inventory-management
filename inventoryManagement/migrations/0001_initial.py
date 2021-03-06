# Generated by Django 2.0.5 on 2018-07-09 09:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import inventoryManagement.modelFiles.CustomCharField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='deviceList',
            fields=[
                ('deviceName', inventoryManagement.modelFiles.CustomCharField.TitleCaseCharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'List Of Devices',
            },
        ),
        migrations.CreateModel(
            name='Historicalrecord',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', inventoryManagement.modelFiles.CustomCharField.TitleCaseCharField(max_length=200, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('department', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('building', inventoryManagement.modelFiles.CustomCharField.TitleCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('year', models.DecimalField(decimal_places=0, max_digits=4, validators=[django.core.validators.MinValueValidator(2016)])),
                ('deviceTag', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(db_index=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_deviceTag', message='The device tag MUST follow the pattern <location_firstLetter>-<department>-<deviceShortName>-<intergerNumber>', regex='^([a-zA-z])(-)((?:[a-zA-Z][a-zA-Z]+))(-)((?:[a-zA-Z][a-zA-Z]+))(-)(\\d+)$')])),
                ('old_device_tag', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50)),
                ('item_description', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=200, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('serial_no', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_serialNo', message='The Serial Number should only contain alphanumeric characters and hypen, with NO consecutive spaces. It should also start and end with only alphanumeric characters', regex='^([a-zA-Z0-9])(\\s)*([a-zA-Z0-9-]+\\s)*([a-zA-Z0-9-])+([a-zA-Z0-9])$')])),
                ('brand', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('model_no', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_serialNo', message='The Serial Number should only contain alphanumeric characters and hypen, with NO consecutive spaces. It should also start and end with only alphanumeric characters', regex='^([a-zA-Z0-9])(\\s)*([a-zA-Z0-9-]+\\s)*([a-zA-Z0-9-])+([a-zA-Z0-9])$')])),
                ('service_tag', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=60)),
                ('floor', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('room', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('remarks', inventoryManagement.modelFiles.CustomCharField.TitleCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('device', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventoryManagement.deviceList')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Record Of Inventory',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', inventoryManagement.modelFiles.CustomCharField.TitleCaseCharField(max_length=200, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('department', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('building', inventoryManagement.modelFiles.CustomCharField.TitleCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('year', models.DecimalField(decimal_places=0, max_digits=4, validators=[django.core.validators.MinValueValidator(2016)])),
                ('deviceTag', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_deviceTag', message='The device tag MUST follow the pattern <location_firstLetter>-<department>-<deviceShortName>-<intergerNumber>', regex='^([a-zA-z])(-)((?:[a-zA-Z][a-zA-Z]+))(-)((?:[a-zA-Z][a-zA-Z]+))(-)(\\d+)$')])),
                ('old_device_tag', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50)),
                ('item_description', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=200, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('serial_no', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_serialNo', message='The Serial Number should only contain alphanumeric characters and hypen, with NO consecutive spaces. It should also start and end with only alphanumeric characters', regex='^([a-zA-Z0-9])(\\s)*([a-zA-Z0-9-]+\\s)*([a-zA-Z0-9-])+([a-zA-Z0-9])$')])),
                ('brand', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('model_no', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_serialNo', message='The Serial Number should only contain alphanumeric characters and hypen, with NO consecutive spaces. It should also start and end with only alphanumeric characters', regex='^([a-zA-Z0-9])(\\s)*([a-zA-Z0-9-]+\\s)*([a-zA-Z0-9-])+([a-zA-Z0-9])$')])),
                ('service_tag', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=60)),
                ('floor', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('room', inventoryManagement.modelFiles.CustomCharField.UpperCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('remarks', inventoryManagement.modelFiles.CustomCharField.TitleCaseCharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_text', message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.', regex='^([a-zA-Z0-9]+\\s)*[a-zA-Z0-9]+$')])),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryManagement.deviceList')),
            ],
            options={
                'verbose_name': 'Record Of Inventory',
                'verbose_name_plural': 'Records Of Inventory',
            },
        ),
        migrations.CreateModel(
            name='recordSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Department Grouped Graph',
                'verbose_name_plural': 'Departments Grouped Graph',
                'proxy': True,
                'indexes': [],
            },
            bases=('inventoryManagement.record',),
        ),
    ]