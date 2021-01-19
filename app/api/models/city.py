from django.contrib.gis.db import models
from .department import Department
from .epci import EPCI


class City(models.Model):
    """ City Model for storing city related data """
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=250)
    department = models.ForeignKey(
        Department,
        related_name='cities',
        on_delete=models.CASCADE,
        null=False
    )
    epci = models.ForeignKey(
        EPCI,
        related_name='cities',
        on_delete=models.CASCADE,
        null=False
    )
