"""
Definition of models.
"""
from django.db import connection
from django.db import models

# Create your models here.

# Create model data.
class Data(models.Model):
    ID_DATA = models.IntegerField() 
    ID_LOCALIZACAO = models.CharField(max_length=10) 
    KMPER_40KM = models.CharField(max_length=10) 
    KMPER_60KM = models.CharField(max_length=10) 
    KMPER_80KM = models.CharField(max_length=10) 
    KMPER_100KM = models.CharField(max_length=10) 
    COSM_40KM = models.CharField(max_length=10) 
    COSM_60KM = models.CharField(max_length=10) 
    COSM_80KM = models.CharField(max_length=10) 
    COSM_100KM = models.CharField(max_length=10) 

# Create model Location.
class Location(models.Model):
    ID_LOCALIZACAO = models.IntegerField()
    PT_PARTIDA = models.CharField(max_length=10)
    PT_CHEGADA = models.CharField(max_length=10)
    CREATED_ATT = models.DateField(editable=False, blank=True, null=True)
    UPDATED = models.DateField(editable=False, blank=True, null=True)
