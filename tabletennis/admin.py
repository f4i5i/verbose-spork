from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

# Register your models here.
from .models import *

class PhasesAdmin(admin.ModelAdmin):
    list_display = ('key','desc','evkey','phase_type')
    list_filter = (('phase_type',DropdownFilter),
                    ('key',DropdownFilter),)

class CompAdmin(admin.ModelAdmin):
    list_display = ('champ','description','location', 'url')
    list_filter = (('location',DropdownFilter),)
    search_fields = ('champ','location','description')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','short_name')


admin.site.register(Competition,CompAdmin)
admin.site.register(RawData)
admin.site.register(Phases,PhasesAdmin)
admin.site.register(Table)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Country,CountryAdmin)
admin.site.register(MatchRawData)
admin.site.register(Team)

