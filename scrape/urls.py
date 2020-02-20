from django.urls import path,include

from .views import HomeView,scrapeview,IttfView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('scrape',scrapeview,name='web_scrape'),
    path('table',IttfView.as_view(),name='ittf'),

]