from django.contrib.gis.db import models
from .address import Address


class Building(models.Model):
    """ Building Model for storing building related data """
    entry = models.CharField(max_length=20, null=True)
    batiment = models.CharField(max_length=25, null=True)
    immeuble = models.CharField(max_length=250, null=True)
    compl = models.CharField(max_length=50, null=True)
    address = models.ForeignKey(
        Address,
        related_name='buildings',
        on_delete=models.CASCADE,
        null=False
    )
