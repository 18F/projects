from rest_framework import viewsets, serializers
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from projects import models


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = (
            'name',
            'slug',
            'tagline',
            'project_lead',
            'description',
            'impact',
            'live_site_url',
            'github_url',
            'status',
            'billable',
            'cloud_dot_gov',
            'tock_id',
            'mb_number',
        )


class ReadOnlyViewSet(RetrieveModelMixin, ListModelMixin,
                      viewsets.GenericViewSet):
    pass


class ProjectsViewSet(ReadOnlyViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return models.Project.objects.all()
