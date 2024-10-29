from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render


def password_reset_view(request):
    return render(request, 'authenticate/ResetPass.html')


def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Applicant_signup.html')
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")

    return render(request, 'Applicant_signup.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("home")
