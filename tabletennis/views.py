from django.shortcuts import render, HttpResponse

import django_rq
# Create your views here.
from .tasks import scrape
from .models import Phases

def view1(request):
    queue = django_rq.get_queue('default',is_async=True,default_timeout=30000)
    queue.enqueue(scrape)
    return HttpResponse("Scraping..........")

def view2(request):
    phase = Phases.objects.all()
    return HttpResponse(phase[1].id)
