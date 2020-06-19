from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=254)
    country = models.ForeignKey(Country,related_name="countrypartof",on_delete=models.PROTECT)
    subcountry = models.CharField(max_length=254)
    geonameid = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sport(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name

class Player(models.Model):
    first_name = models.TextField(max_length=1000)
    last_name = models.TextField(max_length=1000)
    gender =  models.CharField(max_length=100)
    dob = models.CharField(max_length=254)
    sport = models.ForeignKey(Sport,related_name="playersport",on_delete=models.PROTECT)
    country = models.ForeignKey(Country,related_name="playercountry",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class CompetitionType(models.Model):
    name = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    snid = models.IntegerField()
    tsname = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tsname


class Competition(models.Model):
    trnid = models.AutoField(primary_key=True)
    trnname = models.TextField(max_length=1000)
    sptid = models.ForeignKey(Sport,related_name="sport",on_delete=models.PROTECT)
    cntid = models.ForeignKey(Country,related_name="country",on_delete=models.PROTECT,blank=True,null=True)
    turid = models.ForeignKey(CompetitionType,related_name="comptype",on_delete=models.PROTECT)
    snid = models.ForeignKey(Season,related_name="compseason",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trnname



class Draw(models.Model):
    draw_type = models.CharField(max_length=254)
    code = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.draw_type

class Round(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
