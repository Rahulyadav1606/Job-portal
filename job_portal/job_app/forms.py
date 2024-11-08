from django import forms
from Applicant.models import Application

class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'})
        }

class ScheduleInterviewForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['interview_time']
        widgets = {
            'interview_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
