from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView
import  django_rq
from django.shortcuts import HttpResponseRedirect,HttpResponse
import xml.etree.ElementTree as ET
from django.shortcuts import render
import re

from .tasks import scrape
from .models import Players,Matches,Tournament,TournamentInfo

class HomeView(TemplateView):
    template_name = 'home.html'



def scrapeview(request):
    if request.method == "GET":
        queue= django_rq.get_queue('default',is_async=True,default_timeout=30000)
        queue.enqueue(scrape)
    return HttpResponse("Scraping..........")





def playerxml2(request):
     if request.method == "GET":
        data1 = Players.objects.all().values_list()
        a = ET.Element('Players')
        for i in range(len(data1)):
            b = ET.SubElement(a,'player',id=str(data1[i][0]))
            x = ET.SubElement(b,'match')
            x.text = str(Matches.objects.get(pk=data1[i][1]))
            c = ET.SubElement(b,'home')
            c.text = data1[i][2].capitalize().replace('/',' & ')
            d = ET.SubElement(b,'away')
            d.text = data1[i][3].capitalize().replace('/',' & ')
            y = ET.SubElement(b,'TeamA')
            y.text = data1[i][10]
            z = ET.SubElement(b,'TeamB')
            z.text = data1[i][11]

        res = ET.tostring(a)
        return HttpResponse(res,content_type="application/xml")


def tournamentinfo(request):
    if request.method == "GET":
        data = TournamentInfo.objects.all().values_list()
        a = ET.Element('TournamentData')
 

        for i in range(len(data)):
            b = ET.SubElement(a,'Tournmanetid',id=str(data[i][0]))
            # c = ET.SubElement(b,'URL')
            # c.text = str(data[i][1])
            d = ET.SubElement(b,'champ')
            d.text = str(data[i][2])
            # # e = ET.SubElement(b,'status')
            # e.text = data[i][3]
            # f = ET.SubElement(b,'dates')
            # f.text = data[i][4]
            # g = ET.SubElement(b,'datesdesc')
            # g.text = data[i][5]
            h = ET.SubElement(b,'champdesc')
            h.text = data[i][6]
            j = ET.SubElement(b,'location')
            j.text = data[i][7]
            # g = ET.SubElement(b,'events')
            # g.text = data[i][8]
            temp = data[i][9].strip()
            temp = temp.replace("[","")
            temp = temp.replace("]","")
            temp = list(temp.split(","))
            k = ET.SubElement(b,'phases')
            for j in temp:
                n = ET.SubElement(k,'phase')
                n.text = j
            # l = ET.SubElement(b,'locations')
            # l.text = data[i][10]
        res = ET.tostring(a)
        # return HttpResponse(temp[1])
        return HttpResponse(res,content_type="application/xml")







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


