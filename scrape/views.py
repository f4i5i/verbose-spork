from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView
import  django_rq
from django.shortcuts import HttpResponseRedirect,HttpResponse
import xml.etree.ElementTree as ET
from django.shortcuts import render

from .tasks import scrape
from .models import Players,Matches,Tournament,TournamentInfo

class HomeView(TemplateView):
    template_name = 'home.html'



def scrapeview(request):
    if request.method == "GET":
        queue= django_rq.get_queue('default',is_async=True,default_timeout=30000)
        queue.enqueue(scrape)
    return HttpResponse("Scraping..........")


class IttfView(ListView):
    model = Players
    template_name = "Table.html"


def playerxml(request):
    if request.method == "GET":
        data1 = Players.objects.all().values_list()
        res = data1[1]
        return HttpResponse(res)

def playerxml2(request):
     if request.method == "GET":
        data1 = Players.objects.all().values_list()
        a = ET.Element('Players')
        for i in range(len(data1)):
            b = ET.SubElement(a,'player',id=str(data1[i][0]))
            c = ET.SubElement(b,'home')
            c.text = data1[i][2]
            d = ET.SubElement(b,'away')
            d.text = data1[i][3]

        res = ET.tostring(a)
        return HttpResponse(res,content_type="application/xml")

    
def matches(request):
    if request.method == "GET":
        data = Matches.objects.all().values_list()
        a = ET.Element('Matches')
       
    return HttpResponse(data[1])

def tournament(request):
    if request.method == "GET":
        data = TournamentInfo.objects.all().values_list()
        data1 = data[0][1]
        a = ET.Element('Matches')
       
    return HttpResponse(data)

def fixtures(request):
    if request.method == "GET":
        data = Matches.objects.all().values_list()
        a = ET.Element('fixtures')
        for i in range(len(data)):
            b = ET.SubElement(a,'fixture_id',id=str(data[i][0]))
            c = ET.SubElement(b,'time')
            c.text = data[i][4]
            d = ET.SubElement(b,'rtime')
            d.text = data[i][8]
        res = ET.tostring(a)
        return HttpResponse(res,content_type="application/xml")