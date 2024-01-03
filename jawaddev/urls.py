"""
URL configuration for jawaddev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import handler404, handler500
from core.views import custom_404_view, custom_500_view
from home import views

handler404 = custom_404_view
handler500 = custom_500_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('contact/',views.contact_me,name='contact'),
    path('cv/',views.CvView.as_view(),name='cv'),
    path('download-cv/', views.download_cv, name='download_cv'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('',include('user.urls')),
    path('reading-list/',include('readinglist.urls')),
    path('portfolio/',include('portfolio.urls')),
    path('blog/',include('blog.urls')),
    path('api/',include('api.urls', namespace='api')),
    # path('pdf-to-docx/',include('pdftodocx.urls')),
    path('bake-picker/',include('bakepicker.urls')),
    path('expense-tracker/profile/',include('expensetracker.urls')),
    path('scraping/',include('scraping.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)