from django.urls import path,include
from .views import view1,view2,view3,view4,view5,PlayersXml,view6

urlpatterns = [
    path('',view1,name="view1"),
    path('v2',view2,name="view2"),
    path('v3',view3,name="view3"),
    path('v4',view4,name="view4"),
    path('v5',view5,name="view5"),
    path('v6',view6,name="view6"),
    path('Players',PlayersXml,name="playersfeed"),

]