from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostReadOnlyApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rest_framework/api.html'