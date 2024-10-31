from .models import Applicant, Application, Resume,SavedJob



def applicant_context(request):
    applicant = None
    has_resume = False
    applied_jobs_count = 0
    saved_jobs_count = 0  # New variable for saved jobs count

    applicant_id = request.session.get('applicant_id')
    if applicant_id:
        try:
            applicant = Applicant.objects.get(id=applicant_id)
            applied_jobs_count = Application.objects.filter(applicant=applicant).count()
            saved_jobs_count = SavedJob.objects.filter(applicant=applicant).count()  # Count saved jobs
            has_resume = Resume.objects.filter(applicant=applicant).exists()
        except Applicant.DoesNotExist:
            pass

    return {
        'applicant': applicant,
        'has_resume': has_resume,
        'applied_jobs_count': applied_jobs_count,
        'saved_jobs_count': saved_jobs_count,  # Include saved jobs count in context
    }

