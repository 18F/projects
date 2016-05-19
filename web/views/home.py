from django.views.generic import ListView

from projects.models import Project


class HomeView(ListView):
    context_object_name = 'projects'
    model = Project
    ordering = '-created'
    paginate_by = 24
    template_name = 'web/index.html'
