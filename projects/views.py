from django.db.models import Q
from dal import autocomplete

from .models import Client


class ClientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        user = self.request.user

        if not (user.is_authenticated() and user.is_staff):
            return Client.objects.none()

        qs = Client.objects.all()

        if self.q:
            qs = qs.filter(
                Q(department__icontains=self.q) |
                Q(agency__icontains=self.q)
            )

        return qs
