from django.shortcuts import render
from django.views.generic  import TemplateView, ListView
from .models import Project, ProjectCategory

# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/components/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        return context

    def get_queryset(self):

        category = self.request.GET.get('category')

        print(category)

        if category:
            return Project.objects.filter(categories=category)

        return Project.objects.all()