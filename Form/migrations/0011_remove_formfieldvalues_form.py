# Generated by Django 4.2.7 on 2025-04-18 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0010_masterdropdowndata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfieldvalues',
            name='form',
        ),
    ]
