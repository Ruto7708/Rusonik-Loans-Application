from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect




from .forms import LoanApplicationForm


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import LoanApplication  # Assuming you have a LoanApplication model


# Create your views here.
def layout(request):
    return render(request, 'dashboard/layout.html')
@login_required()
def dashboard(request):
    return render(request,'dashboard/dashboard.html')
def apply_now(request):
    return render(request,'dashboard/apply_now.html')

#
# @login_required
# def dashboard(request):
#     return render(request, 'dashboard/dashboard.html')

@login_required
def apply_now(request):
    if request.method == 'POST':
        # Handle form submission here
        loan_amount = request.POST['loan_amount']
        loan_duration = request.POST['loan_duration']
        loan_purpose = request.POST['loan_purpose']

        # Process the loan application (save it to the database, etc.)
        # You can add the loan details to the user's profile, or to a separate Loan model
        # For example, saving to a Loan model
        # Loan.objects.create(user=request.user, amount=loan_amount, duration=loan_duration, purpose=loan_purpose)

        # Redirect to a confirmation page or back to the dashboard
        return redirect('dashboard')

    return render(request, 'dashboard/dashboard.html')


# @login_required
# def submit_loan_application(request):
#     if request.method == "POST":
#         loan_amount = request.POST.get('loan_amount')
#         loan_duration = request.POST.get('loan_duration')
#         loan_purpose = request.POST.get('loan_purpose')
#
#         # Save the loan application
#         loan_app = LoanApplication(
#             user=request.user,
#             loan_amount=loan_amount,
#             loan_duration=loan_duration,
#             loan_purpose=loan_purpose
#         )
#         loan_app.save()
#
#         messages.success(request, "Loan application submitted successfully!")
#         return redirect('dashboard')  # Redirect to the dashboard or any other page
#
#     return HttpResponse("Invalid request method", status=405)


def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def repay_loan(request):
    return render(request,'dashboard/repay_loan.html')
@login_required
def view_status(request):
    # Mock data for demonstration purposes
    loan_status = {
        "status": "Pending",  # Options: "Verified", "Pending", "Rejected"
        "stage": "Document Verification",  # Stage the loan is currently in
        "remarks": "Please upload the required documents to proceed."
    }

    return render(request, 'dashboard/view_status.html', {"loan_status": loan_status})
def apply_now(request):
    return render(request,'dashboard/apply_now.html')

def bootstrap_layout(request):
    return render(request, 'dashboard/bootstraplayout.html')


from django.shortcuts import render, redirect
from .models import LoanApplication
from django.contrib import messages

@login_required()
def submit_loan_application(request):
    if request.method == 'POST':
        # Collect form data
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        loan_amount = request.POST['loan_amount']
        loan_duration = request.POST['loan_duration']
        employment_status = request.POST['employment_status']
        id_number = request.POST['id_number']
        address = request.POST['address']

        # Save to the database
        LoanApplication.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            loan_amount=loan_amount,
            loan_duration=loan_duration,
            employment_status=employment_status,
            id_number=id_number,
            address=address
        )
        messages.success(request, "Your loan application has been submitted!")
        return redirect('apply_now')  # Replace 'apply_now' with your desired redirect URL

    return render(request, 'dashboard/apply_now.html')  # Adjust template name if necessary





import requests
from django.shortcuts import render, redirect
from .forms import LoanRepaymentForm, EmployerAgreementForm

def repay_loan(request):
    repayment_form = LoanRepaymentForm()
    employer_form = EmployerAgreementForm()
    error = None

    if request.method == 'POST':
        if 'amount' in request.POST:  # Loan repayment form
            repayment_form = LoanRepaymentForm(request.POST)
            if repayment_form.is_valid():
                repayment = repayment_form.save(commit=False)
                repayment.borrower = request.user
                repayment.save()
                # M-Pesa API Call
                response = mpesa_payment(repayment.phone_number, repayment.amount)
                if response['ResponseCode'] == '0':
                    return redirect('success_page')  # Replace with your success redirect
                else:
                    error = response.get('errorMessage', 'Payment failed. Try again.')
        elif 'employer_name' in request.POST:  # Employer agreement form
            employer_form = EmployerAgreementForm(request.POST, request.FILES)
            if employer_form.is_valid():
                agreement = employer_form.save(commit=False)
                agreement.borrower = request.user
                agreement.save()
                return redirect('employer_aagreement_success')  # Replace with your success redirect

    return render(request, 'dashboard/repay_loan.html', {
        'repayment_form': repayment_form,
        'employer_form': employer_form,
        'error': error
    })

def mpesa_payment(phone_number, amount):
    # Replace these with your Daraja API credentials
    consumer_key = '2bgxUKmGSEAVwTQy3P67WFfbL8DIsKEKGN0XubepuzEs0zuX'
    consumer_secret = 'w7MxbfwQT81jbO6HMySpTkJRuQTULNgu1GbfzAmp5qTy6BoU4Mr2CQ1gGoG9ezvU'
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    # Obtain access token
    auth_response = requests.get(access_token_url, auth=(consumer_key, consumer_secret))
    access_token = auth_response.json().get('access_token')

    payment_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {'Authorization': f'Bearer {access_token}'}
    payload = {
        "BusinessShortCode": "174379",
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",
        "Timestamp": "20160216165627",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "amount",
        "PartyA": "phone_number",
        "PartyB": "174379",
        "PhoneNumber": "254708374149",
        "CallBackURL": "https://mydomain.com/pat",
        "AccountReference": "Test",
        "TransactionDesc": "Test"
    }
    response = requests.post(payment_url, json=payload, headers=headers)
    return response.json()


@login_required
def view_status(request):
    # Mock data for demonstration purposes
    loan_status = {
        "status": "Pending",  # Options: "Verified", "Pending", "Rejected"
        "stage": "Document Verification",  # Stage the loan is currently in
        "remarks": "Please upload the required documents to proceed."
    }

    return render(request, 'dashboard/view_status.html', {"loan_status": loan_status})


def employer_aagreement_success(request):
    return render(request, 'dashboard/employer_aagreement_success.html')