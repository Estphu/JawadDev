from django.shortcuts import render
from django.views.generic  import TemplateView

# Create your views here.
class ProjectView(TemplateView):
    template_name = 'projects/project_view.html'