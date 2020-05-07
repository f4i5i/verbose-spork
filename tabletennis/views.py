from django.shortcuts import render, HttpResponse
import requests
import xml.etree.ElementTree as ET
import django_rq
from datetime import timedelta

# Create your views here.
from .tasks import scrape
from .models import *
from .utils2 import *
from .playerscraper import *


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


def view4(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(get_player_data)
    return HttpResponse("Scraping Players..........")

def view5(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(get_match_data)
    return HttpResponse("Scraping Matches..........")

