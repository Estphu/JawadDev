from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Book
from user.models import Profile
from portfolio.models import Project
from blog.models import Post

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=12)
        context["projects"] = Project.objects.filter(user=12)
        context["posts"] = Post.objects.filter(author=12)
        return context

class ReadingListView(ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(user=12)
    


class CVView(TemplateView):
    template_name = 'home/cv.html'      

def contact_me(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                f"Message From Portfolio Contact Form By {form.cleaned_data['firstname']} {form.cleaned_data['lastname']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['jawad4world@gmail.com']
            )
            form = ContactForm()
            return render(request, 'home/contact.html', {'form': form, 'msg_sent': True})

    return render(request, 'home/contact.html', {'form': form})         
