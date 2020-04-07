from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
import xml.etree.ElementTree as ET
from .models import *


class PlayerListView(ListView):
    queryset = Player.objects.all()
    def get_queryset(self):
        qs = super(PlayerListView,self).get_queryset()
        return PlayerFilter(data=self.request.GET,queryset=qs).filter()


def playerview(request,id,country,sport):
    if request.method == "GET":
        player = Player.objects.filter(country=country)
        #p_name = p_name.split(' ')[-1]+","+" ".join(p_name.split(' ')[:-1])

        return HttpResponse(player)

def testview(request):
    para1 = request.GET.get('id')
    para2 = request.GET.get('name')
    para3 = request.GET.get('country')

    res = para1 + " " + para2 + " " + para3 

    return HttpResponse(res)