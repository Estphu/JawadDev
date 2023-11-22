from .models import Profile

def profile(request, pk=12):
    profile = Profile.objects.get(user=pk)
    return {
        'full_name': f'{profile.user.first_name} {profile.user.last_name}',
        'avatar_url': profile.avatar.url
    }