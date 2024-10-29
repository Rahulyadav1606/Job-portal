# Generated by Django 5.1.1 on 2024-10-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0011_remove_applicant_password_alter_applicant_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]