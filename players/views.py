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
    filter_args = request.GET.dict()
    new_dict = {}
    for k,v in filter_args.items():
        if v != None:
            new_dict.update({k:v})

   

    return HttpResponse(new_dict.values())