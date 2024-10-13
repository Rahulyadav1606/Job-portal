from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm


def resume(request):
    resumes = Resume.objects.all()
    return render(request, 'resume.html', {'resumes': resumes})


def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Redirect to the resume list page
    else:
        form = ResumeForm()

    return render(request, 'upload_resume.html', {'form': form})
