from django.urls import path, re_path

from .views import PlayerListView,playerview,testview

urlpatterns = [
    path('details/<int:id>/<int:country>/<int:sport>',playerview,name="PlayersFilterView"),
    path('test/',testview,name='test'),
]