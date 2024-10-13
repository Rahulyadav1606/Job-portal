from django.contrib import admin
from .models import Applicant


admin.site.register(Applicant)


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')