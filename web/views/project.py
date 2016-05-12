from django.views.generic.detail import DetailView

from projects.models import Project


class ProjectView(DetailView):
    context_object_name = 'project'
    model = Project
    template_name = 'web/project.html'
