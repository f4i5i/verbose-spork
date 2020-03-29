from django.shortcuts import render, HttpResponse
import requests
import xml.etree.ElementTree as ET


import django_rq
# Create your views here.
from .tasks import scrape
from .models import Phases,RawData,Competition,MatchRawData
from .utils2 import get_match_urls,get_country,get_player_data
from .playerscraper import get_match_data


def view1(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(scrape)
    return HttpResponse("Scraping Competitions..........")

def view2(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(get_match_urls)
    return HttpResponse("Scraping Match Urls..........")

def view3(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(get_country)
    return HttpResponse("Scraping Country's..........")


# def view4(request):
#     queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
#     queue.enqueue(get_player_data)
#     return HttpResponse("Scraping Players..........")

# def view5(request):
#     queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
#     queue.enqueue(get_match_data)
#     return HttpResponse("Scraping Matches..........")


# def PlayersXml(request):
#     allPlayers = Player.objects.all().values_list()
#     root_element = ET.Element('Players')
#     for i in range(len(allPlayers)):
#         ply = ET.SubElement(root_element,'Player',id=str(allPlayers[i][0]))
#         name = ET.SubElement(ply,'PlayerName')
#         name.text = allPlayers[i][1]
#         country = ET.SubElement(ply,'Country')
#         db_country = Country.objects.get(pk=allPlayers[i][2])
#         country.text = db_country.name
#         gender = ET.SubElement(ply,'Gender')
#         gender.text = allPlayers[i][3]
#         dob = ET.SubElement(ply,'DOB')
#         dob.text = allPlayers[i][4]
#         sport = ET.SubElement(ply,'Sport')
#         sport.text = allPlayers[i][6]
    
#     xmlfeed = ET.tostring(root_element)
#     return HttpResponse(xmlfeed,content_type="application/xml")

# def view6(request):
#     data =  MatchRawData.objects.all().values_list()
#     data1 = data[2][2][1]
#     return HttpResponse(data1)