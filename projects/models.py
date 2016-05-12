from django.db import models


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(ModelBase):
    name = models.CharField(
        max_length=100,
        help_text='The full name of the project (e.g., "Agile BPA")'
    )
    slug = models.CharField(
        max_length=100,
        help_text='The slug of the project (e.g., "agile-bpa")'
    )
    tock_id = models.IntegerField(
        help_text='The ID of the project in Tock.',
        blank=True,
        null=True,
        unique=True
    )
    tagline = models.CharField(
        max_length=300,
        help_text='The tagline of the project; short and concise.'
    )
    impact = models.TextField(
        help_text='The impact of the project. Markdown is allowed.'
    )
    live_site_url = models.URLField(
        help_text='A URL to the site where the project is deployed, '
                  'if one exists.',
        blank=True
    )
    github_url = models.URLField(
        help_text='The GitHub URL of the project, e.g. '
                  'https://github.com/18f/agile-bpa',
        blank=True
    )
    description = models.TextField(
        help_text='The description of the project. Markdown is allowed.'
    )
    active = models.BooleanField(
        help_text='Whether or not the project is currently being '
                  'worked on at 18F.',
        default=True
    )
