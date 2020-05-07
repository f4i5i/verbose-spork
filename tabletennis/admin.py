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

admin.site.register(RawData)
admin.site.register(Player,PlayerAdmin)
admin.site.register(TTCompetition)
admin.site.register(MatchUrl,MatchUrlAdmin)
admin.site.register(RawMatchData)
admin.site.register(Match)
admin.site.register(Team)   
admin.site.register(Single)
admin.site.register(Double)
admin.site.register(MatchScrapingError,MatchScrapingErrorAdmin)   

