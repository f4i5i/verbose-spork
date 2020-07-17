from django.urls import path, re_path

from .views import PlayerXML,TourXML,StageXML,double_player, matchXML

urlpatterns = [
    path('players',PlayerXML,name='xmlfunc'),
    path('tours',TourXML,name='tourxml'),
    path('stages', StageXML, name='stagexml'),
    path('doubleplayers', double_player, name='double_player'),
    path('match', matchXML , name='matchxml'),
]
