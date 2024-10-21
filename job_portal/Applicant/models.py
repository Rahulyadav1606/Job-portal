from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
class Applicant(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)

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
