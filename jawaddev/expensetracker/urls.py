from django.urls import path
from . import views

app_name = 'expensetracker'

urlpatterns = [
    path('add/', views.ExpenseProfileCreateView.as_view(), name='expense_profile_form'),
    path('profile/<slug:slug>/', views.expense_tracker_view, name='expense_tracker_view'),
    path('verify/', views.expense_profile_verify,name='expense_profile_verify')
]
