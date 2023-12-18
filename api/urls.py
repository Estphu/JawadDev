from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostAPIView

app_name = 'api'

router = DefaultRouter()

router.register(r'posts', PostAPIView, basename='post')

urlpatterns = [
    path('blog/',include(router.urls))
]
