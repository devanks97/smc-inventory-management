# Generated by Django 2.0.5 on 2018-05-22 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryManagement', '0002_auto_20180522_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='department',
        ),
        migrations.RemoveField(
            model_name='record',
            name='device',
        ),
        migrations.RemoveField(
            model_name='record',
            name='year',
        ),
    ]
