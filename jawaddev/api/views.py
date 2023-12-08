from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from blog.models import Post
from .serializers import PostSerializer

class PostAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer