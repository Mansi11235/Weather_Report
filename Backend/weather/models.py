from django.db import models

# Creat your models here.
class Weather(models.Model):
    # id = models.IntegerField(primary_key=True)
    date = models.DateField()
    maximum_temp = models.FloatField(null=True)
    minimum_temp = models.FloatField(null=True)
    precipitation = models.FloatField(null=True)
    state_code = models.CharField(max_length=20,default='', null=True)

class Statistics(models.Model):
    year = models.IntegerField()
    average_minimum = models.FloatField(null=True)
    average_maximum = models.FloatField(null=True, default=0)
    total_precipitation = models.FloatField(null=True, default=0)
    state_code = models.CharField(max_length=20,default='', null=True)
            