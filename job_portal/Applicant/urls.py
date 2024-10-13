from django.urls import path
from . import views

from django.urls import path
from . import views
from .views import Applicant_dashboard

urlpatterns = [
    path('applicant_dashboard/', Applicant_dashboard, name='Applicant_dashboard'),
    path('applicant_signup/', views.applicant_signup, name='applicant_signup'),
    path('applicant_login/', views.applicant_login, name='applicant_login'),
    path('applicant_logout/', views.applicant_logout, name='applicant_logout'),

]
