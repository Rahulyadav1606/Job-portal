# Generated by Django 5.1.1 on 2024-10-29 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0009_applicant_user'),
        ('job_app', '0007_job_applicants_delete_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Applicant.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_app.job')),
            ],
        ),
    ]