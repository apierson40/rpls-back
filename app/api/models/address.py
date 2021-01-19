from django.contrib.gis.db import models
from .city import City


class Address(models.Model):
    """ Address Model for storing address related data """
    num = models.CharField(max_length=20, null=True)
    repetition_indice = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=500)
    locality = models.CharField(max_length=500, null=True)
    postal_code = models.IntegerField()
    city = models.ForeignKey(
        City,
        related_name='addresses',
        on_delete=models.CASCADE,
        null=False
    )
