from django.urls import path
from django.contrib.auth import views as authviews
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'user'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('login/',authviews.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',authviews.LogoutView.as_view(),name='logout'),
    path('profile/<slug:slug>',views.profile,name='profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)