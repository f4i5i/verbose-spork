from django.urls import path,include
from .views import view1,view2,view3,view4

urlpatterns = [
    path('',view1,name="view1"),
    path('v2',view2,name="view2"),
    path('v3',view3,name="view3"),
    path('v4',view4,name="view4"),
]