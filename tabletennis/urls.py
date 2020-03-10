from django.urls import path,include
from .views import view1,view2

urlpatterns = [
    path('',view1,name="view1"),
    path('v2',view2,name="view2"),

]