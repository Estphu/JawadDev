from typing import Any
from django.shortcuts import render
from django.views.generic  import TemplateView, ListView
from .models import Project

# Create your views here.
class ProjectView(TemplateView):
    template_name = 'portfolio/project.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.filter(user=3)
        return context