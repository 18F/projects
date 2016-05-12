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

    def __str__(self):
        return '%s - %s' % (self.department, self.agency)


class Project(ModelBase):
    name = models.CharField(max_length=256)
    client = models.ForeignKey(Client, null=True)
    description = models.TextField()
