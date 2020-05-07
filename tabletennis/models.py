from django.db import models
import os
from django_mysql.models import JSONField
# Create your models here.
from players.models import City,Player,Competition



class RawData(models.Model):
    name = models.TextField()
    url = models.TextField()
    raw_data = JSONField()
    tour_type = models.CharField(max_length=254)
    is_finished = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Error(models.Model):
    url = models.TextField()
    error = models.TextField()
    extra_info = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Player(models.Model):
    player_id = models.CharField(primary_key=True,max_length=200)
    player_key = models.ForeignKey(Player,related_name="playermain",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  


class TTCompetition(models.Model):
    tour_id = models.CharField(primary_key=True,max_length=254)
    competition_id = models.ForeignKey(Competition,related_name="competitionid",on_delete=models.PROTECT)
    finished = models.BooleanField()
    gender = models.CharField(max_length=254)
    m_type = models.CharField(max_length=254)
    startdate = models.CharField(max_length=254)
    enddate = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    

class MatchUrl(models.Model):
    match_url = models.TextField()
    champ_id = models.ForeignKey(TTCompetition,related_name="TTCompUrls",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Event(models.Model):
    champ_events = models.ForeignKey(TTCompetition,related_name="TTCompEvent",on_delete=models.PROTECT)
    event_key = models.CharField(max_length=254)
    event_desc = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Phase(models.Model):
    champ_phase = models.ForeignKey(TTCompetition,related_name="TTCompPhase",on_delete=models.PROTECT)
    phase_key = models.CharField(max_length=254)
    phase_desc = models.CharField(max_length=254)
    phase_evkey = models.CharField(max_length=254)
    phase_type = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


class RawMatchData(models.Model):
    tt_champ = models.ForeignKey(TTCompetition,related_name="TTCompRawData",on_delete=models.PROTECT)
    data_json = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


class Match(models.Model):
    match_date = models.CharField(max_length=254)
    tourn_id = models.ForeignKey(TTCompetition,related_name="TTCompMatch",on_delete=models.PROTECT)
    ppstatus = models.CharField(max_length=254)
    m_time = models.CharField(max_length=254)
    venue = models.TextField()
    m_number = models.CharField(max_length=254)
    event = models.ForeignKey(Event,related_name="MatchEvent",on_delete=models.PROTECT)
    phase = models.ForeignKey(Phase,related_name="MatchPhase",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Team(models.Model):
    player_1 = models.ForeignKey(Player,related_name="P1Team",on_delete=models.PROTECT)
    player_2 = models.ForeignKey(Player,related_name="P2Team",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class Single(models.Model):
    home = models.ForeignKey(Player,related_name="HomePly",on_delete=models.PROTECT)
    away = models.ForeignKey(Player,related_name="AwayPly",on_delete=models.PROTECT)
    match = models.ForeignKey(Match,related_name="SingleMatch",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Double(models.Model):
    home_T = models.ForeignKey(Team,related_name="HomeTeam",on_delete=models.PROTECT)
    away_T = models.ForeignKey(Team,related_name="AwayTeam",on_delete=models.PROTECT)
    match = models.ForeignKey(Match,related_name="DoubleMatch",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class MatchScrapingError(models.Model):
    error = models.TextField()
    champ = models.ForeignKey(TTCompetition,related_name="ChampError",on_delete=models.PROTECT)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
