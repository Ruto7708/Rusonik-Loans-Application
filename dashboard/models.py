from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LoanApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_duration = models.PositiveIntegerField()  # Duration in months
    loan_purpose = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan Application by {self.user.username} - {self.loan_amount}"


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
#
# class LoanApplication(models.Model):
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     loan_duration = models.IntegerField()
#     employment_status = models.CharField(max_length=50)
#     id_number = models.CharField(max_length=50)
#     address = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.full_name


from django.db import models

class LoanApplicationForms(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_duration = models.IntegerField(help_text="Duration in months")
    employment_status = models.CharField(max_length=50, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')])
    id_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan Application by {self.full_name} - {self.loan_amount} KES"

    class Meta:
        verbose_name = "Loan Application Form"
        verbose_name_plural = "Loan Application Forms"





class LoanRepayment(models.Model):
    borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Loan Repayment"
        verbose_name_plural = "Loan Repayments"


class EmployerAgreement(models.Model):
    borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=255)
    employer_contact = models.CharField(max_length=15)
    agreement_file = models.FileField(upload_to='agreements/')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Employer Agreement"
        verbose_name_plural = "Employer Agreements"

