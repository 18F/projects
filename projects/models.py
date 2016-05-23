from functools import reduce
from operator import or_

from django.db import models
from django.db.models import Q


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(models.Model):
    department = models.CharField(
        help_text='Deparment is the highest organizational level.',
        max_length=255,
        blank=True
    )
    agency = models.CharField(
        help_text='Agency is the level below the Department.',
        max_length=255,
        blank=True
    )
    omb_agency_code = models.CharField(
        help_text='OMB Agency Code is the top level code.',
        max_length=255,
        blank=True,
        verbose_name='OMB Agency Code'
    )
    omb_bureau_code = models.CharField(
        help_text='OMB Bureau Code is the level below OMB Agency Code.',
        max_length=255,
        blank=True,
        verbose_name='OMB Bureau Code'
    )
    treasury_agency_code = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Treasury Agency Code'
    )
    cgac_agency_code = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='CGAC Agency Code'
    )

    class Meta:
        ordering = ['department', 'agency']

    def __str__(self):
        return '%s - %s' % (self.department, self.agency)


class ProjectManager(models.Manager):
    def search(self, terms):
        qs = self.get_queryset()
        terms = [term.strip() for term in terms.split()]

        if not terms:
            return qs

        q_objs = []
        for term in terms:
            q_objs.append(Q(name__icontains=term))
            q_objs.append(Q(tagline__icontains=term))

        return qs.filter(reduce(or_, q_objs))


class Project(ModelBase):
    name = models.CharField(
        max_length=100,
        help_text='The full name of the project (e.g., "Agile BPA")'
    )
    slug = models.CharField(
        max_length=100,
        help_text='The slug of the project (e.g., "agile-bpa")',
        blank=True
    )
    tagline = models.CharField(
        max_length=300,
        help_text='The tagline of the project; short and concise.',
        blank=True
    )
    client = models.ForeignKey(
        Client,
        help_text='The client of the project, if any.',
        blank=True,
        null=True
    )
    project_lead = models.CharField(
        help_text='Name of 18F employee who is responsible for this'
        ' project.',
        max_length=255,
        verbose_name='Project Lead',
        blank=True
    )
    description = models.TextField(
        help_text='The description of the project. Markdown is allowed.'
    )
    impact = models.TextField(
        help_text='The impact of the project. Markdown is allowed.',
        blank=True
    )
    live_site_url = models.URLField(
        help_text='A URL to the site where the project is deployed, '
                  'if one exists.',
        blank=True,
        verbose_name='Live URL'
    )
    github_url = models.URLField(
        help_text='The GitHub URL of the project, e.g. '
                  'https://github.com/18f/agile-bpa',
        blank=True,
        verbose_name='GitHub URL'
    )
    status = models.IntegerField(
        help_text='Current status of the project.',
        choices=[
            (0, 'Tentative'), (1, 'Active'), (2, 'Paused'), (3, 'Complete')
        ],
        default=1
    )
    billable = models.IntegerField(
        help_text='Whether or not the project is chargeable to a'
        ' non-18F client.',
        choices=[(0, 'Billable'), (1, 'Non-billable')],
        default=1
    )
    cloud_dot_gov = models.BooleanField(
        help_text='Whether or not the project includes cloud.gov '
        'platform support.',
        default=False,
        verbose_name='Cloud.gov Project'
    )
    tock_id = models.IntegerField(
        help_text='The ID of the project in Tock.',
        blank=True,
        null=True,
        unique=True,
        verbose_name='Tock ID'
    )
    mb_number = models.CharField(
        help_text='The unique identifier for an agreement in'
        'the GSA financial system. This is different than'
        'the Tock ID.',
        max_length=100,
        blank=True,
        verbose_name='MB Number'
    )
    is_visible = models.BooleanField(
        help_text='Projects with a primary private repos should'
        'be listed as false. All other projects should be '
        'listed as true.',
        default=False,
        verbose_name='Is visible (in dashboard)?'
    )

    objects = ProjectManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
