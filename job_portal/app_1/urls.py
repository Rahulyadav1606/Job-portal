from django.urls import path
from . import views
from .views import upload_resume

urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('upload-resume/', upload_resume, name='upload_resume'),
]
