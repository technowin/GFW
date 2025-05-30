# Generated by Django 4.2.7 on 2025-05-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0060_formfieldvalues_file_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionControlFileMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField(blank=True, null=True)),
                ('form_data_id', models.IntegerField(blank=True, null=True)),
                ('form_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'version_control_file_map',
            },
        ),
    ]
