from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume, Applicant,Application

def applicant_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Applicant_signup.html')

        try:
            # Create applicant and hash the password
            applicant = Applicant(name=name,username=username, email=email)
            applicant.set_password(password)  # Hash password
            applicant.save()

            messages.success(request, "Applicant account created successfully. You can now log in.")
            return redirect('applicant_login')
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")

    return render(request, 'Applicant_signup.html')


def Applicant_dashboard(request):
    applicant_id = request.session.get('applicant_id')
    applied_jobs_count = 0
    if applicant_id:
        try:
            applicant = Applicant.objects.get(id=applicant_id)
            applied_jobs_count = Application.objects.filter(applicant=applicant).count()
            has_resume = Resume.objects.filter(applicant=applicant).exists()
        except Applicant.DoesNotExist:
            applicant = None
            has_resume = False
    else:
        applicant = None
        has_resume = False

    return render(request, 'Applicant_dashboard.html', {
        'applicant': applicant,
        'has_resume': has_resume,
        'applied_jobs_count': applied_jobs_count,
        'request': request
    })



def applicant_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            applicant = Applicant.objects.get(username=username)

            if applicant.check_password(password):
                request.session['applicant_id'] = applicant.id
                return redirect('Applicant_dashboard')
            else:
                messages.error(request, "Invalid username or password")
        except Applicant.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, 'Applicant_login.html')


def resume(request):
    resumes = Resume.objects.all()
    return render(request, 'resume.html', {'resumes': resumes})



def upload_resume(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')
        recruiter_name = request.POST.get('recruiter_name')
        recruiter_email = request.POST.get('recruiter_email')
        recruiter_position = request.POST.get('recruiter_position')
        applicant_id = request.session.get('applicant_id')  # Get the logged-in applicant's ID

        if resume_file and recruiter_name and recruiter_email and recruiter_position and applicant_id:
            Resume.objects.create(
                applicant_id=applicant_id,  # Set the applicant_id
                resume_file=resume_file,
                recruiter_name=recruiter_name,
                recruiter_email=recruiter_email,
                recruiter_position=recruiter_position
            )
            messages.success(request, "Resume uploaded successfully.")
            return redirect('Applicant_dashboard')
        else:
            messages.error(request, "Please provide all required fields and ensure you are logged in.")

    return render(request, 'upload_resume.html')


# views.py
from django.shortcuts import render

def view_applied_jobs(request):
    applicant_id = request.session.get('applicant_id')  # Get the applicant ID from the session
    if not applicant_id:  # If there's no applicant ID in the session, redirect to login
        return redirect('applicant_login')

    # Retrieve the current logged-in applicant
    applicant = get_object_or_404(Applicant, id=applicant_id)

    # Filter the applications for the current applicant
    applied_jobs = Application.objects.select_related('job').filter(applicant=applicant)

    return render(request, 'view_applied_jobs.html', {'applied_jobs': applied_jobs})




def applicant_logout(request):
    request.session.flush()  # Clear the session data
    return redirect('Applicant_login')
