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

class CityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','country' )
    search_fields = ('name',)


class PlayerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'gender', 'dob', 'sport', 'country')
    search_fields = ('first_name', 'last_name',)

class CompTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('snid', 'tsname')
    search_fields = ('tsname',)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("trnid",'trnname','sptid','cntid','turid','snid')

class DrawAdmin(admin.ModelAdmin):
    list_display =("draw_type","code")

class RoundAdmin(admin.ModelAdmin):
    list_display = ("name","code")

class GroupAdmin(admin.ModelAdmin):
    list_display = ("name","code")

class QualificationAdmin(admin.ModelAdmin):
    list_display=("name","code")







admin.site.register(Country,CountryAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(CompetitionType,CompTypeAdmin)
admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Draw,DrawAdmin)
admin.site.register(Round,RoundAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Qualification,QualificationAdmin)

