from django.contrib import admin
from .models import ExpenseProfile, ExpenseTracker

# Register your models here.
admin.site.register(ExpenseProfile)
admin.site.register(ExpenseTracker)
