from django.db import models


# Create your models here.

# class Ittf(models.Model):
    
#     urlfortournement = models.TextField(max_length=500)
#     tournment_name = models.TextField(max_length=500)
#     tournment_location = models.TextField(max_length=500)
#     tournment_desc = models.TextField(max_length=500)
#     isfinished = models.BooleanField()
#     match_desc = models.TextField(max_length=500)
#     match_time = models.TextField(max_length=500)
#     isteam = models.BooleanField(max_length=500)
#     home = models.TextField(max_length=500)
#     away = models.TextField(max_length=500)
#     teamA = models.TextField(max_length=500,null=True,blank=True)
#     team2 = models.TextField(max_length=500,null=True,blank=True)


class Tournament(models.Model):
    urlfortournement = models.URLField(max_length=1000)
    
    def __str__(self):
        return self.urlfortournement


class NotScraped(models.Model):
    urlfornotscraped = models.URLField(max_length=1000)

    def __str__(self):
        return self.urlfornotscraped

        
class TournamentInfo(models.Model):
    urltournement = models.ForeignKey(Tournament,related_name="urlfortour",on_delete=models.CASCADE)
    champ = models.TextField(max_length=1000)
    status = models.TextField(max_length=1000)
    dates = models.TextField(max_length=1000)
    datesdesc = models.TextField(max_length=1000)
    champdesc = models.TextField(max_length=1000)
    location = models.TextField(max_length=1000)
    events = models.TextField(max_length=1000)
    phases = models.TextField(max_length=1000)
    locations = models.TextField(max_length=1000)
    isfinished = models.BooleanField()

    def __str__(self):
        return self.champ

class Matches(models.Model):
    champ = models.ForeignKey(TournamentInfo,related_name="champinfo",on_delete=models.CASCADE)
    key = models.TextField(max_length=1000)
    desc = models.TextField(max_length=1000)
    time = models.TextField(max_length=1000)
    loc = models.TextField(max_length=1000)
    locdesc = models.TextField(max_length=1000)
    venue = models.TextField(max_length=1000)
    rtime = models.TextField(max_length=1000)
    status= models.TextField(max_length=1000)
    isteam = models.TextField(max_length=1000)
    hascomps = models.TextField(max_length=1000)

    def __str__(self):
        return self.key

class Players(models.Model):
    match = models.ForeignKey(Matches,related_name="match",on_delete=models.CASCADE)
    home = models.TextField(max_length=1000)
    away = models.TextField(max_length=1000)
    home_reg = models.TextField(max_length=1000)
    home_org = models.TextField(max_length=1000)
    home_orgdesc = models.TextField(max_length=1000)
    away_reg = models.TextField(max_length=1000)
    away_org = models.TextField(max_length=1000)
    away_orgdesc = models.TextField(max_length=1000)
    team_a = models.TextField(max_length=1000,null=True,blank=True)
    team_b = models.TextField(max_length=1000,null=True,blank=True)
    
        