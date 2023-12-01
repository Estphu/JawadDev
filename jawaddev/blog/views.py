from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

# Create your views here.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'