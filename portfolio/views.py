from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic  import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project, ProjectReview

# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'

class ProjectCreatView(LoginRequiredMixin, CreateView):
    template_name = "portfolio/project_form.html"
    success_url = reverse_lazy('portfolio:project_list')
    model = Project
    fields = ['title', 'thumbnail', 'btn_title', 'desc', 'link', 'categories', 'featured']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
    

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "portfolio/project_form.html"
    success_url = reverse_lazy('portfolio:project_list')
    model = Project
    fields = ['title', 'thumbnail', 'btn_title', 'desc', 'link', 'categories', 'featured']

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "portfolio/project_confirm_delete.html"
    success_url = reverse_lazy('portfolio:project_list')
    model = Project

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = ProjectCategory.objects.all()
    #     return context

    # def get_queryset(self):

    #     category = self.request.GET.get('category')

    #     print(category)

    #     if category:
    #         return Project.objects.filter(categories=category)

    #     return Project.objects.all()

class ProjectReview(DetailView):
    model = ProjectReview
    template_name = 'portfolio/project_review.html'
    context_object_name = 'project_review'
    slug_url_kwarg = 'slug'
