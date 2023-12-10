from django.urls import path
from . import views

app_name = 'expensetracker'

urlpatterns = [
    path('<str:username>/', views.expense_tracker_view, name='expense_tracker_view'),
    path('create/', views.ExpenseProfileCreateView.as_view(), name='expense_profile_form'),
    path('verify/', views.ExpenseProfileVerifyView.as_view(),name='expense_profile_verify')
]
