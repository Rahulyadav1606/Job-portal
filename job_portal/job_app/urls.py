from django.urls import path
from . import views
from .views import add_job_view, update_job, ManageJobsView, delete_job, job_list,job_list1


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('index/', views.index, name='index'),  # Index page
    path('job-list/', job_list, name='job_list'),
    path('job-list1/', job_list1, name='job_list1'),
    path('loginsignup/', views.loginsignup, name='loginsignup'),
    path('manage-jobs/', ManageJobsView.as_view(), name='Managejobs'),
    path('update-job/<int:job_id>/', update_job, name='update_job'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('delete_job/<int:job_id>/', delete_job, name='delete_job'),
    path('contact/', views.contact_view, name='contact'),
    path('addjob/', views.add_job_view, name='Addjob'),
]

