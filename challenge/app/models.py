"""
Definition of models.
"""
from django.db import connection
from django.db import models
import MySQLdb

# Create your models here.
class Data(models.Model):
    id_localizacao = models.CharField(max_length=10) 
    kmper_40km = models.CharField(max_length=10) 
    kmper_60km = models.CharField(max_length=10) 
    kmper_80km = models.CharField(max_length=10) 
    kmper_100km = models.CharField(max_length=10) 
    cosm_40km = models.CharField(max_length=10) 
    cosm_60km = models.CharField(max_length=10) 
    cosm_80km = models.CharField(max_length=10) 
    cosm_100km = models.CharField(max_length=10)
    

    sql = "select * from data"
    cursor = connection.cursor()
    try:
        cursor.execute(sql, ['localhost'])
        row = cursor.fetchall()
    except Exception as e:
        cursor.close
