from django.urls import path, re_path

from .views import PlayerXML

urlpatterns = [
    path('players',PlayerXML,name='xmlfunc'),
]