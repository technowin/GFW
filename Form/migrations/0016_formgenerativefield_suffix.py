# Generated by Django 4.2.7 on 2025-04-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0015_remove_formgenerativefield_suffix'),
    ]

    operations = [
        migrations.AddField(
            model_name='formgenerativefield',
            name='suffix',
            field=models.TextField(blank=True, null=True),
        ),
    ]
