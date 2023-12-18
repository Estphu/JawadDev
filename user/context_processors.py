from django.urls import reverse
from .models import Profile

def profile(request, pk=3):
    profile = Profile.objects.get(user=pk)
    return {
        'full_name': f'{profile.user.first_name} {profile.user.last_name}',
        'avatar_url': profile.avatar.url
    }

def url_names(request):
    return {
        'blog_url': reverse('blog:post_list'),
        'blog_api_url': reverse('api:post-list'),
        # 'pdf_to_docx_url': reverse('pdftodocx:pdftodocxconverter'),
        'expense_tracker_url': reverse('expensetracker:expense_profile_form')
    }