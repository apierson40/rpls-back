from django.contrib.gis.db import models
from .address import Address
from .building import Building
from .parcel import Parcel


class Housing(models.Model):
    """ Housing Model for storing housing related data """
    num_apartment = models.CharField(max_length=20, null=True)
    num_box = models.IntegerField(null=True)
    staircase = models.CharField(max_length=10, null=True)
    hall = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    compl = models.CharField(max_length=50, null=True)
    qpv = models.IntegerField()
    type_const = models.CharField(max_length=2)
    nb_piece = models.CharField(max_length=2)
    surface = models.IntegerField()
    construct = models.IntegerField()
    locate = models.IntegerField()
    patrimoine = models.IntegerField()
    origine = models.CharField(max_length=2)
    finanture = models.CharField(max_length=250, null=True)
    conv = models.IntegerField()
    num_conv = models.CharField(max_length=250, null=True)
    sru_expir = models.IntegerField(null=True)
    date_conv = models.CharField(max_length=10, null=True)
    new_logt = models.IntegerField(null=True)
    dpe_date = models.CharField(max_length=10, null=True)
    dpe_energie = models.CharField(max_length=2, null=True)
    dpe_serre = models.CharField(max_length=2, null=True)
    sru_alinea = models.CharField(max_length=2, null=True)
    code_seg_patrim = models.CharField(max_length=50, null=True)
    lib_seg_patrim = models.CharField(max_length=250, null=True)
    cus = models.CharField(max_length=2, null=True)
    droit = models.CharField(max_length=2)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    geom = models.PointField(null=True)
    address = models.ForeignKey(
        Address,
        related_name='housings',
        on_delete=models.CASCADE,
        null=False
    )
    building = models.ForeignKey(
        Building,
        related_name='housings',
        on_delete=models.CASCADE,
        null=True
    )
    parcel = models.ForeignKey(
        Parcel,
        related_name='housings',
        on_delete=models.CASCADE,
        null=True
    )
