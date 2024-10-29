from django.contrib import admin
from .models import Applicant,Resume,Application


admin.site.register(Applicant)

admin.site.register(Resume)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(Application)