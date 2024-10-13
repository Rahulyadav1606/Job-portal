from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume_file', 'recruiter_name', 'recruiter_email', 'recruiter_position']
