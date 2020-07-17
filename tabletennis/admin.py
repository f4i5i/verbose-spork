from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

# Register your models here.
from .models import *

class MatchUrlAdmin(admin.ModelAdmin):
    list_display = ('match_url','champ_id')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id','player_key')
    search_fields = ('player_id','player_key')

class MatchScrapingErrorAdmin(admin.ModelAdmin):
    list_display = ('error','champ','desc')


class TTCompetitionAdmin(admin.ModelAdmin):
    list_display = ('tour_id','competition_id','gender','startdate','enddate')


class DoubleAdmin(admin.ModelAdmin):
    list_display = ('home_T', 'away_T', 'match')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('player_1', 'player_2')


class RawMatchDataAdmin(admin.ModelAdmin):
    list_display = ('tt_champ', 'created_at')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_date', 'm_time', 'tourn_id', 'phase')
    search_fields = ('id','tourn_id')
class PhaseAdmin(admin.ModelAdmin):
    list_display = ('champ_phase','phase_key','phase_desc','phase_evkey','phase_type')

class EventAdmin(admin.ModelAdmin):
    list_display = ('champ_events','event_key','event_desc')

admin.site.register(RawData)
admin.site.register(Error)
admin.site.register(Player,PlayerAdmin)
admin.site.register(TTCompetition,TTCompetitionAdmin)
admin.site.register(MatchUrl,MatchUrlAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(RawMatchData,RawMatchDataAdmin)
admin.site.register(Match,MatchAdmin)
admin.site.register(Team,TeamAdmin)   
admin.site.register(Single)
admin.site.register(Double,DoubleAdmin)
admin.site.register(MatchScrapingError,MatchScrapingErrorAdmin)   

