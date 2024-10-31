from .models import Job

def recruiter_context(request):
    if request.user.is_authenticated:
        # Assuming the `user` field in Job relates to the recruiter
        jobs = Job.objects.filter(user=request.user).order_by('-created_at')
    else:
        jobs = Job.objects.none()

    return {
        'recruiter_jobs': jobs,
        'is_recruiter': request.user.is_authenticated,
    }