from django.db import models


# Create your models here.

# class Ittf(models.Model):
    
#     urlfortournement = models.CharField(max_length=500)
#     tournment_name = models.CharField(max_length=500)
#     tournment_location = models.CharField(max_length=500)
#     tournment_desc = models.CharField(max_length=500)
#     isfinished = models.BooleanField()
#     match_desc = models.CharField(max_length=500)
#     match_time = models.CharField(max_length=500)
#     isteam = models.BooleanField(max_length=500)
#     home = models.CharField(max_length=500)
#     away = models.CharField(max_length=500)
#     teamA = models.CharField(max_length=500,null=True,blank=True)
#     team2 = models.CharField(max_length=500,null=True,blank=True)


class Tournament(models.Model):
    urlfortournement = models.URLField(max_length=1000)
    
    def __str__(self):
        return self.urlfortournement

class TournamentInfo(models.Model):
    urltournement = models.ForeignKey(Tournament,related_name="urlfortour",on_delete=models.CASCADE)
    champ = models.CharField(max_length=1000)
    status = models.CharField(max_length=1000)
    dates = models.CharField(max_length=1000)
    datesdesc = models.CharField(max_length=1000)
    champdesc = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    events = models.CharField(max_length=1000)
    phases = models.CharField(max_length=1000)
    locations = models.CharField(max_length=1000)
    isfinished = models.BooleanField()

class Matches(models.Model):
    champ = models.ForeignKey(TournamentInfo,related_name="champinfo",on_delete=models.CASCADE)
    key = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    time = models.CharField(max_length=1000)
    loc = models.CharField(max_length=1000)
    locdesc = models.CharField(max_length=1000)
    venue = models.CharField(max_length=1000)
    rtime = models.CharField(max_length=1000)
    status= models.CharField(max_length=1000)
    isteam = models.CharField(max_length=1000)
    hascomps = models.CharField(max_length=1000)


class Players(models.Model):
    match = models.ForeignKey(Matches,related_name="match",on_delete=models.CASCADE)
    home = models.CharField(max_length=1000)
    away = models.CharField(max_length=1000)
    hasstats = models.CharField(max_length=1000)
    team_a = models.CharField(max_length=1000,null=True,blank=True)
    team_b = models.CharField(max_length=1000,null=True,blank=True)

        