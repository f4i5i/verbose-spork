from django.db import models
import os
# Create your models here.

class RawData(models.Model):
    raw_data = models.TextField(max_length=10000)
    

class Phases(models.Model):
    key = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    evkey = models.CharField(max_length=100)
    phase_type = models.CharField(max_length=100)

    
    def __str__(self):
        return self.desc

class Table(models.Model):
    key = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)





class Competition(models.Model):
    champ = models.CharField(primary_key=True,max_length=100)
    description = models.TextField(max_length=1000)
    location = models.TextField(max_length=1000)
    isfinished = models.BooleanField()
    url = models.URLField(max_length=1000)
    compdates = models.TextField(max_length=1000)
    raw_comp = models.ForeignKey(RawData,related_name="competition_rawdata",on_delete=models.CASCADE,blank=True,null=True)






# class Player(models.Model):
#     pass


# class Country(models.Model):
#     pass

