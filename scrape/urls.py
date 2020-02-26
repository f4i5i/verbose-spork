from django.urls import path,include

from .views import HomeView,scrapeview,IttfView,playerxml2,playerxml,matches,tournament,fixtures


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('scrape',scrapeview,name='web_scrape'),
    path('table',IttfView.as_view(),name='ittf'),
    path('xml',playerxml,name='xml'),
    path('xml2',playerxml2,name='xml2'),
    path('xml3',matches,name='xml3'),
    path('xml4',tournament,name='xml4'),
    path('fixtures',fixtures,name="fixtures"),


]