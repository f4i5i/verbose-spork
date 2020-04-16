from django.urls import path, re_path

from .views import PlayerXML,TourXML

urlpatterns = [
    path('players',PlayerXML,name='xmlfunc'),
    path('tours',TourXML,name='tourxml'),
]