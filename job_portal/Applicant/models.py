from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from job_app.models import Job


class Applicant(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Resume(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume_file = models.FileField(upload_to='resumes/')
    recruiter_name = models.CharField(max_length=150)
    recruiter_email = models.EmailField()
    recruiter_position = models.CharField(max_length=150)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume of {self.applicant.username} - {self.recruiter_position}"


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"


class SavedJob(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)