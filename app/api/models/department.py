from django.contrib.gis.db import models
from .region import Region


class Department(models.Model):
    """ Department Model for storing department related data """
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=250)
    region = models.ForeignKey(
        Region,
        related_name='departments',
        on_delete=models.CASCADE,
        null=False
    )
