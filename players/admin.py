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

class CompTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')


class PlayerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','gender','dob','sport','country')


admin.site.register(Country,CountryAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(CompetitionType,CompTypeAdmin)
admin.site.register(Competition)
admin.site.register(Season)