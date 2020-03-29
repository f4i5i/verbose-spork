from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sport(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Player(models.Model):
    name = models.TextField(1000)
    gender =  models.CharField(max_length=100)
    dob = models.DateField(blank=True,null=True)
    sport = models.ForeignKey(Sport,related_name="playersport",on_delete=models.PROTECT)
    country = models.ForeignKey(Country,related_name="playercountry",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Competition(models.Model):
    name = models.TextField(max_length=1000)
    sport = models.ForeignKey(Sport,related_name="sport",on_delete=models.PROTECT)
    country = models.ForeignKey(Country,related_name="country",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



