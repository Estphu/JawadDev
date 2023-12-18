from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, View, CreateView
from .models import ExpenseProfile, ExpenseTracker
from .forms import ExpenseProfileVerifyForm

# Create your views here.
class ExpenseProfileCreateView(CreateView):
    model = ExpenseProfile
    fields = ['username', 'balance', 'income', 'question', 'answer']
    # success_url = reverse('expensetracker:expense_tracker_view', kwargs={'slug':})

    def get_success_url(self):
        print(self.object)
        return reverse_lazy('expensetracker:expense_tracker_view', kwargs={'slug': self.object.slug})

def expense_tracker_view(request, slug):
    try:
        profile = ExpenseProfile.objects.get(slug=slug)
        expenses = ExpenseTracker.objects.filter(profile=profile.id)
        if(profile is None):
            return redirect('expensetracker:expense_profile_verify')
        else:
            if request.method == 'POST':
                text = request.POST.get('text')
                amount = request.POST.get('amount')
                expense_type = request.POST.get('expense_type')
                expense = ExpenseTracker(expense_text=text,amount=amount,expense_type=expense_type,profile=profile)
                expense.save()
                if(expense_type == 'Positive'):
                    profile.balance += float(amount)
                else:
                    profile.expense += float(amount)
                    profile.balance -= float(amount)
                profile.save()
                return redirect(reverse_lazy('expensetracker:expense_tracker_view', kwargs={'slug': profile.slug}))
        context = {'profile':profile, 'expenses':expenses}
        return render(request, 'expensetracker/expense_tracker.html',context=context)
    except ExpenseProfile.DoesNotExist:
        return redirect('expensetracker:expense_profile_form')
    
# class ExpenseProfileVerifyView(FormView):
#     template_name = 'expensetracker/expense_profile_verify.html'
#     form_class = ExpenseProfileVerifyForm

#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)

#     def form_valid(self, form):
#         # Extract information entered by the user
#         username_value = form.cleaned_data.get('username')
#         question_value = form.cleaned_data.get('question')
#         answer_value = form.cleaned_data.get('answer')

#         # Example: Custom validation with existing values in the model
#         is_profile_exists = ExpenseProfile.objects.filter(username=username_value, question=question_value, answer=answer_value)

#         if is_profile_exists.exists():
#             # If a matching profile is found, redirect to the expense tracker view
#             return redirect(reverse_lazy('expensetracker:expense_tracker_view', kwargs={'slug': is_profile_exists.slug}))
#         else:
#             return redirect(reverse_lazy('expensetracker:expense_tracker_view'))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

def expense_profile_verify(request):
    if request.method == 'POST':
        form = ExpenseProfileVerifyForm(request.POST)

        print(form.is_valid())

        print(form.errors)

        if form.is_valid():
            # Extract information entered by the user
            username_value = form.cleaned_data.get('username')

            print(username_value)
            print(form.cleaned_data.get('question'))
            print(form.cleaned_data.get('answer'))


            # Match the entered information with existing expense profiles
            profile = ExpenseProfile.objects.get(username=username_value)

            print(profile)
            return redirect(reverse_lazy('expensetracker:expense_tracker_view', kwargs={'slug': profile.slug}))
        else:
            # If no matching profile is found, you can render a template or redirect to another view as needed
            # return render(request, 'no_matching_profile.html')
            return redirect(reverse('expensetracker:expense_profile_verify'))
    else:
        form = ExpenseProfileVerifyForm()

    return render(request, 'expensetracker/expense_profile_verify.html', {'form': form})



    