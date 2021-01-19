from django.contrib.gis.db import models


class Region(models.Model):
    """ Region Model for storing region related data """
    code = models.IntegerField()
    name = models.CharField(max_length=250)
