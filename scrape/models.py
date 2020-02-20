from django.db import models


# Create your models here.

class Ittf(models.Model):
    
    urlfortournement = models.CharField(max_length=500)
    tournment_name = models.CharField(max_length=500)
    tournment_location = models.CharField(max_length=500)
    tournment_desc = models.CharField(max_length=500)
    isfinished = models.BooleanField()
    match_desc = models.CharField(max_length=500)
    match_time = models.CharField(max_length=500)
    isteam = models.BooleanField(max_length=500)
    home = models.CharField(max_length=500)
    away = models.CharField(max_length=500)
    teamA = models.CharField(max_length=500,null=True,blank=True)
    team2 = models.CharField(max_length=500,null=True,blank=True)
