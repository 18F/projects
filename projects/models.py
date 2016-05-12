from django.db import models


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(models.Model):
    department = models.CharField(max_length=255, blank=True)
    agency = models.CharField(max_length=255, blank=True)
    omb_agency_code = models.CharField(max_length=255, blank=True)
    omb_bureau_code = models.CharField(max_length=255, blank=True)
    treasury_agency_code = models.CharField(max_length=255, blank=True)
    cgac_agency_code = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['department', 'agency']

    def __str__(self):
        return '%s - %s' % (self.department, self.agency)


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
    tock_id = models.IntegerField(
        help_text='The ID of the project in Tock.',
        blank=True,
        null=True,
        unique=True
    )
    tagline = models.CharField(
        max_length=300,
        help_text='The tagline of the project; short and concise.',
        blank=True
    )
    impact = models.TextField(
        help_text='The impact of the project. Markdown is allowed.',
        blank=True
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
    client = models.ForeignKey(
        Client,
        help_text='The client of the project, if any.',
        null=True
    )
    billable = models.BooleanField(
        help_text='Whether or not the project is chargeable to a client.',
        default=False
    )
    mb_number = models.CharField(
        help_text='The unique identifier for an agreement in'
        'the GSA financial system. This is different than'
        'the tock_id.',
        max_length=100,
        blank=True
    )
    cloud_dot_gov = models.BooleanField(
        help_text='Whether or not the project includes cloud.gov'
        'platform support.',
        default=False
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
