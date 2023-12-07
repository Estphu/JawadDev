from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostReadOnlyApiView

app_name = 'api'

router = DefaultRouter()

router.register(r'posts', PostReadOnlyApiView, basename='post')

urlpatterns = [
    path('blog/',include(router.urls))
]
