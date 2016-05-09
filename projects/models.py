from django.db import models


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(ModelBase):
    name = models.CharField(max_length=256)
    description = models.TextField()
