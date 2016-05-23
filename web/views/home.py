from django.views.generic import ListView

from projects.models import Project


class HomeView(ListView):
    context_object_name = 'projects'
    model = Project
    ordering = '-created'
    paginate_by = 100
    template_name = 'web/index.html'

    def get_queryset(self):
        qs = super(HomeView, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            qs = self.model.objects.search(q)

        return qs

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context.update(self.search_stats() or {})

        return context

    def search_stats(self):
        q = self.request.GET.get('q')

        if not q:
            return

        return {
            'query': q,
            'total': self.get_queryset().count(),
        }
