from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post
from .forms import PostSearchForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    form_class = PostSearchForm

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['form'] = self.form_class(self.request.GET)
        context['query'] = self.request.GET.get('query', '')
        return context  

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'