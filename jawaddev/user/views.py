from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views import View
from .forms import UserRegisterForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/register.html'

    def get_success_url(self):
        return reverse('user:profile', kwargs={'profile_slug': self.slug})
    
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('home') # Redirect back to home page

    else:
        p_form = UpdateProfileForm(instance=request.user.profile)

    print(p_form.fields)
    
    context = {
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)
