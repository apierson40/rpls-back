from django.contrib.gis.db import models
from .department import Department


class EPCI(models.Model):
    """ EPCI Model for storing epci related data """
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=250)
    departments = models.ManyToManyField(Department, related_name="epcis")
