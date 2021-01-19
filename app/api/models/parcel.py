from django.contrib.gis.db import models


class Parcel(models.Model):
    """ Parcel Model for storing parcel related data """
    housing_count = models.IntegerField()
    geom = models.MultiPolygonField()
