from django.urls import path,include

from .views import HomeView,scrapeview,playerxml2,tournamentinfo,fixtures


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('scrape',scrapeview,name='web_scrape'),
    path('xml2',playerxml2,name='xml2'),
    path('info',tournamentinfo,name='infoxml'),
    path('fixtures',fixtures,name="fixtures"),

]