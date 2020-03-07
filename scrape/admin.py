from django.contrib import admin

# Register your models here.
from .models import Tournament,TournamentInfo,Matches,Players,NotScraped

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('match','home','home_org','away','away_org',)
    list_filter = ('home_org','away_org')
    search_fields = ('home','away',)



class MatchAdmin(admin.ModelAdmin):
    list_display = ('champ','key','desc','time','loc','venue','isteam',)
    search_fields = ('champ','key','venue',)
    list_filter = ('isteam','loc') 


admin.site.register(Players,PlayerAdmin)
admin.site.register(Tournament)
admin.site.register(TournamentInfo)
admin.site.register(Matches, MatchAdmin)
admin.site.register(NotScraped)