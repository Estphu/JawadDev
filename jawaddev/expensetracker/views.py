from django.shortcuts import redirect, render
from django.views.generic import View, CreateView
from .models import ExpenseProfile, ExpenseTracker
from .forms import ExpenseProfileForm

# Create your views here.
class ExpenseProfileCreateView(CreateView):
    template_name = 'expensetracker/expense_profile_form.html'
    model = ExpenseProfile
    fields = ['username', 'balance', 'income', 'question', 'answer']

def expense_tracker_view(request, username):
    try:
        profile = ExpenseProfile.objects.get(username=username)
        expenses = ExpenseTracker.objects.filter(profile=profile.id)
        if(profile is None):
            return redirect('expensetracker:expense_profile_verify')
        else:
            if request.method == 'POST':
                text = request.POST.get('text')
                amount = request.POST.get('amount')
                expense_type = request.POST.get('expense_type')
                expense = ExpenseTracker(expense_text=text,amount=amount,expense_type=expense_type,user=request.user)
                expense.save()
                if(expense_type == 'Positive'):
                    profile.balance += float(amount)
                else:
                    profile.expense += float(amount)
                    profile.balance -= float(amount)
                profile.save()
                return redirect('/')
        context = {'profile':profile, 'expenses':expenses}
        return render(request, 'expensetracker/expense_tracker.html',context=context)
    except ExpenseProfile.DoesNotExist:
        return redirect('expensetracker:expense_profile_verify')

class ExpenseProfileVerifyView(View):
    def get(self, request):
        form = ExpenseProfileForm()
        return render(request, 'expensetracker/expense_profile_verify.html', {'form': form})

    def post(self, request):
        form = ExpenseProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # Redirect to the expense tracker view after successful verification
            return redirect('expensetracker:expense_tracker_view', username=username)

        return render(request, 'expensetracker/expense_profile_verify.html', {'form': form})



    