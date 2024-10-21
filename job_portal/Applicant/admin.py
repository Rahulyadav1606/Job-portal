from django.contrib import admin
from .models import Applicant,Resume


admin.site.register(Applicant)

admin.site.register(Resume)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')