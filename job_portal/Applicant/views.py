from audioop import reverse

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import Applicant  # Import your Applicant model
from django.contrib.auth.hashers import make_password
def applicant_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'applicant_signup.html')

        try:
            # Create applicant and hash the password
            applicant = Applicant(username=username, email=email)
            applicant.set_password(password)  # Using set_password method to hash password
            applicant.save()

            messages.success(request, "Applicant account created successfully. You can now log in.")
            return redirect('applicant_login')
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")

    return render(request, 'applicant_signup.html')




def Applicant_dashboard(request):
    return render(request,'Applicant_dashboard.html',context={'request': request})


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

    return render(request, 'applicant_login.html')





def applicant_logout(request):
    if 'applicant_id' in request.session:
        del request.session['applicant_id']
    return redirect('applicant_login')
