from django import forms
from .models import LoanApplication, LoanApplicationForms


class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplicationForms
        fields = ['full_name', 'email', 'phone', 'loan_amount', 'loan_duration', 'employment_status', 'id_number', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


from django import forms
from .models import LoanRepayment, EmployerAgreement

class LoanRepaymentForm(forms.ModelForm):
    class Meta:
        model = LoanRepayment
        fields = ['name', 'amount', 'phone_number']  # Include the 'name' field
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
        }

class EmployerAgreementForm(forms.ModelForm):
    class Meta:
        model = EmployerAgreement
        fields = ['employer_name', 'employer_contact', 'agreement_file']
        widgets = {
            'employer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employer name'
            }),
            'employer_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employer contact'
            }),
            'agreement_file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
