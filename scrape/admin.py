from django.contrib import admin

# Register your models here.
from .models import Tournament,TournamentInfo,Matches,Players

admin.site.register(Tournament)
admin.site.register(TournamentInfo)
admin.site.register(Matches)
admin.site.register(Players)