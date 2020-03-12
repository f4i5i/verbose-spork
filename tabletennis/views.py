from django.shortcuts import render, HttpResponse
import requests

import django_rq
# Create your views here.
from .tasks import scrape
from .models import Phases,RawData,Competition
from .utils2 import get_match_urls,get_country,get_player_data

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
    return HttpResponse("Scraping Country..........")


def view4(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(get_player_data)
    return HttpResponse("Scraping Players..........")
