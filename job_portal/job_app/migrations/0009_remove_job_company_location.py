# Generated by Django 5.1.1 on 2024-11-03 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0008_job_company_location_job_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_location',
        ),
    ]
