from django.db import models

class Resume(models.Model):
    resume_file = models.FileField(upload_to='resumes/')
    recruiter_name = models.CharField(max_length=100)
    recruiter_email = models.EmailField()
    recruiter_position = models.CharField(max_length=100)

    def __str__(self):
        return self.recruiter_name