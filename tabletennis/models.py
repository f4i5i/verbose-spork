from django.db import models
import os
# Create your models here.

class RawData(models.Model):
    raw_data = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Phases(models.Model):
    key = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    evkey = models.CharField(max_length=100)
    phase_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.desc

class Table(models.Model):
    key = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Competition(models.Model):
    champ = models.CharField(primary_key=True,max_length=100)
    description = models.TextField(max_length=1000)
    location = models.TextField(max_length=1000)
    isfinished = models.BooleanField()
    url = models.URLField(max_length=1000)
    compdates = models.TextField(max_length=1000)
    raw_comp = models.ForeignKey(RawData,related_name="competition_rawdata",on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MatchRawData(models.Model):
    url = models.URLField(max_length=1000)
    json_data = models.TextField(max_length=50000)
    comp = models.ForeignKey(Competition,related_name="competition",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Country(models.Model):
    name = models.CharField(max_length=300)
    short_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Player(models.Model):
    name = models.TextField(max_length=1000)
    org = models.ForeignKey(Country,related_name="country",on_delete=models.CASCADE)
    dob = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    player1 = models.ForeignKey(Player,related_name="player_1",on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player,related_name='player_2',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Match(models.Model):
    comp = models.ForeignKey(Competition,related_name="champ_competition",on_delete=models.CASCADE)
    home = models.ForeignKey(Player,related_name="home",on_delete=models.CASCADE)
    away = models.ForeignKey(Player,related_name="away",on_delete=models.CASCADE)
    team_home = models.ForeignKey(Team,related_name="teams_home",on_delete=models.CASCADE)
    team_away = models.ForeignKey(Team,related_name="teams_away",on_delete=models.CASCADE)
    match = models.CharField(max_length=200)
    time = models.CharField(max_length=100)
    venue = models.CharField(max_length=250)
    phase = models.ForeignKey(Phases,related_name='match_phase',on_delete=models.CASCADE)
    table = models.ForeignKey(Table,related_name="loc",on_delete=models.CASCADE)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


