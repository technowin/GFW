# Generated by Django 4.2.7 on 2025-05-09 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0042_formdata_file_ref'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formfieldvaluestemp',
            old_name='old_field_id',
            new_name='old_field_value_id',
        ),
    ]
