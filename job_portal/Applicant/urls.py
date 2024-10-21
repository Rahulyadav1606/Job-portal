from django.urls import path
from . import views
from .views import Applicant_dashboard, upload_resume
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('applicant_dashboard/', Applicant_dashboard, name='Applicant_dashboard'),
    path('applicant_signup/', views.applicant_signup, name='applicant_signup'),
    path('applicant_login/', views.applicant_login, name='applicant_login'),
    path('applicant_logout/', views.applicant_logout, name='applicant_logout'),
    path('update-jobs/', views.manage_jobs, name='update_jobs'),
    path('resume/', views.resume, name='resume'),
    path('upload-resume/', upload_resume, name='upload_resume'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Updated line
]
