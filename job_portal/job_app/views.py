from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import contact as ContactModel
from datetime import datetime
from .models import sign_up
from django.contrib import messages


from django.shortcuts import render
from .models import Job


def job_list(request):
    jobs = Job.objects.all()

    keyword = request.GET.get('job-keyword')
    location = request.GET.get('location')
    job_type = request.GET.get('job-type')
    industry = request.GET.get('industry')

    # Filter jobs based on the search parameters
    if keyword:
        jobs = jobs.filter(title__icontains=keyword)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type__iexact=job_type)
    if industry:
        jobs = jobs.filter(industry__iexact=industry)

    if request.user.is_authenticated and hasattr(request.user, 'recruiter'):
        jobs = jobs.filter(recruiter=request.user.recruiter)

    return render(request, 'index.html', {'jobs': jobs})



def job_list1(request):

    jobs = Job.objects.all()

    keyword = request.GET.get('job-keyword')
    location = request.GET.get('location')
    job_type = request.GET.get('job-type')
    industry = request.GET.get('industry')

    if keyword:
        jobs = jobs.filter(title__icontains=keyword)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type__iexact=job_type)
    if industry:
        jobs = jobs.filter(industry__iexact=industry)

    return render(request, 'home.html', {'jobs': jobs})


@login_required
def add_job_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        industry = request.POST.get('industry')
        job_type = request.POST.get('job_type')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        requirements = request.POST.get('requirements')
        ideal_candidate = request.POST.get('ideal_candidate')
        availability = 'availability' in request.POST

        new_job = Job(
            title=title,
            industry=industry,
            job_type=job_type,
            location=location,
            salary=salary,
            requirements=requirements,
            ideal_candidate=ideal_candidate,
            availability=availability,
            user=request.user  # Save the user who added the job
        )
        new_job.save()
        messages.success(request, "New Job added.")
        return redirect('Managejobs')

    return render(request, 'Addjob.html')


@login_required
def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)  # Ensure the user can only update their own jobs

    if request.method == 'POST':
        job.title = request.POST['title']
        job.industry = request.POST['industry']
        job.job_type = request.POST['job_type']
        job.location = request.POST['location']
        job.salary = request.POST['salary']
        job.requirements = request.POST['requirements']
        job.ideal_candidate = request.POST['ideal_candidate']
        job.availability = 'availability' in request.POST
        job.save()
        messages.success(request, "Job updated successfully.")
        return redirect('Managejobs')

    return render(request, 'Addjob.html', {'job': job})


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)  # Ensure user can only delete their own jobs
    job.delete()
    messages.success(request, "Job deleted successfully.")
    return redirect('Managejobs')



# from django.shortcuts import render
from .models import Job

from Applicant.models import Applicant,Resume

def home(request):
    jobs = Job.objects.order_by('-created_at')[:9]

    # Get the applicant ID from the session
    applicant_id = request.session.get('applicant_id')
    applicant_username = None
    recruiter_username = None

    # If the applicant is logged in, get their username
    if applicant_id:
        try:
            applicant = Applicant.objects.get(id=applicant_id)
            applicant_username = applicant.username
        except Applicant.DoesNotExist:
            applicant_username = None

    # If the recruiter is logged in, get their username
    if request.user.is_authenticated and not applicant_id:
        recruiter_username = request.user.username  # Assuming the recruiter uses the Django user model

    return render(request, 'home.html', {
        'jobs': jobs,
        'applicant_username': applicant_username,
        'recruiter_username': recruiter_username  # Pass recruiter username to the template
    })


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applicant_id = request.session.get('applicant_id')
    applicant_username = None
    recruiter_username = None
    has_resume = False
    is_applicant = False  # Flag to indicate if the user is an applicant
    # If the applicant is logged in, get their username
    if applicant_id:
        try:
            applicant = Applicant.objects.get(id=applicant_id)
            has_resume = Resume.objects.filter(applicant=applicant).exists()
            applicant_username = applicant.username
            is_applicant = True  # Set the flag to True if an applicant is logged in

        except Applicant.DoesNotExist:
            applicant_username = None
            has_resume = False


    # If the recruiter is logged in, get their username
    if request.user.is_authenticated and not applicant_id:
        recruiter_username = request.user.username

    return render(request, 'ViewDetails.html', {
        'job': job,
        'applicant_username': applicant_username,
        'recruiter_username': recruiter_username,
        'has_resume': has_resume,
        'is_applicant': is_applicant,  # Pass the flag to the template
        'request': request
    })


def index(request):
    if request.user.is_authenticated:
        jobs = Job.objects.filter(user=request.user).order_by('-created_at')
    else:
        jobs = Job.objects.none()

    return render(request, 'index.html', {'jobs': jobs})






def loginsignup(request):
    return render(request,'loginsignup.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')

        new_contact = ContactModel(name=name, age=age, email=email, address=address, date=datetime.today())
        new_contact.save()
        messages.success(request, "Profile details updated.")

    return render(request, 'contact.html')



class ManageJobsView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'Managejobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)




