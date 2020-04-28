from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

# Register your models here.
from .models import *

# class PhasesAdmin(admin.ModelAdmin):
#     list_display = ('key','desc','evkey','phase_type')
#     list_filter = (('phase_type',DropdownFilter),
#                     ('key',DropdownFilter),)

# class CompAdmin(admin.ModelAdmin):
#     list_display = ('champ','description', 'url')
#     list_filter = (('location',DropdownFilter),)
#     search_fields = ('champ','location','description')


# class TableAdmin(admin.ModelAdmin):
#     list_display = ('key','desc')

# class MatchRawAdmin(admin.ModelAdmin):    
#     list_display = ('Competition_id','url')

class MatchUrlAdmin(admin.ModelAdmin):
    list_display = ('match_url','champ_id')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id','player_key')

# admin.site.register(Competition,CompAdmin)
admin.site.register(RawData)
admin.site.register(Player,PlayerAdmin)
admin.site.register(TTCompetition)
admin.site.register(MatchUrl,MatchUrlAdmin)
# admin.site.register(Table,TableAdmin)
admin.site.register(RawMatchData)

