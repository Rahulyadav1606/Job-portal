from django.contrib import admin
# Register your models here.
from .models import contact
from .models import sign_up
from .models import Job


admin.site.register(contact)
# admin.site.register(sign_up)
admin.site.register(Job)