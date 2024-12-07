


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# from .forms import LoanApplicationForm, #UserRegistrationForm
from .models import LoanApplication
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ContactForm
from .models import ContactMessage
from .forms import RegistrationForm









# views.py
import random
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
import africastalking
from .models import User
from .forms import RegistrationForm
from django.conf import settings



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages


from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'loans/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'loans/register.html')

        # Use create_user to save user with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'loans/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate using Django's built-in method
        user = authenticate(request, username=username, password=password)  # username=email if you use email as the username
        if user is not None:
            login(request, user)  # Log the user in and start the session
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('dashboard')  # Redirect to the dashboard or appropriate page
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')

# Home page view
def home(request):
    return render(request, 'loans/home.html')


# About page view
def about(request):
    return render(request, 'loans/about.html')







# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


# View to apply for a loan


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def apply_for_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan_application = form.save(commit=False)
            loan_application.user = request.user  # Associate the loan application with the logged-in user
            loan_application.save()
            return redirect('loan_status')  # Redirect to the loan status page after submission
    else:
        form = LoanApplicationForm()

    return render(request, 'loans/apply_for_loan.html', {'form': form})


# View to display loan application status
@login_required
def loan_status(request):
    user_loans = LoanApplication.objects.filter(user=request.user)
    return render(request, 'loan_status.html', {'user_loans': user_loans})


# views.py



def contact(request):
    if request.method == 'POST':
        # If the form is submitted, validate and save the data
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # Optionally, you can display a success message
            return redirect('success')  # Redirect after successful submission
        else:
            return render(request, 'loans/contact.html', {'form': form, 'error': 'There was an error submitting the form.'})
    else:
        # GET request, just display the form
        form = ContactForm()
        return render(request, 'loans/contact.html', {'form': form})
    
    # views.py
def success(request):
    return render(request, 'loans/contactsucess.html', {'message': 'Your message has been sent successfully.'})

