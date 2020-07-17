from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name','code')
    search_fields = ('name',)
    
@admin.register(Sport)
class SportAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','code')
    search_fields = ('name',)

class PlayerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','gender', 'dob', 'sport', 'country')
    search_fields = ('id','first_name', 'last_name',)

class CompTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('snid', 'tsname')
    search_fields = ('tsname',)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("trnid",'trnname','sptid','cntid','turid','snid')
    search_fields = ('trnid','trname','turid',)



admin.site.register(Country,CountryAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(CompetitionType,CompTypeAdmin)
admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Season, SeasonAdmin)

