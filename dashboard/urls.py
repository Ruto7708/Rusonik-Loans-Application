from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/', views.apply_now, name='apply_now'),

    path('status/', views.view_status, name='view_status'),
    path('repay_loan/', views.repay_loan, name='repay_loan'),
    path('submit-loan-application/', views.submit_loan_application, name='submit_loan_application'),
    path('bootstraplayout', views.bootstrap_layout, name='bootstraplayout'),
    path('application/', views.LoanApplicationForm, name='application'),
    path('employer-agreement-success/', views.employer_aagreement_success, name='employer_aagreement_success'),
]

