import os
import requests
from bs4 import BeautifulSoup
import re
import time
from django_rq import job
from .func import  *
from .models import Ittf
import  django_rq
from datetime import datetime


def scrape():
    HEADERS =  {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}
    url ='https://www.ittf.com/2019-event-calendar/'

    all_urls =get_ittf_url(url)
    f_urls = filter_list(all_urls)
    sub_set = f_urls[12:16]
    sch_list,rv_list = get_daily_schedule(sub_set)
    for url in sch_list:
        new_url = url[:55]+"champ.json"
        print(new_url)
        champ_data = requests.get(new_url,headers=HEADERS,timeout=30).json()
        champName = champ_data['champ']
        champDesc = champ_data['champDesc']
        champLocation = champ_data['location']
        champFinished = champ_data['isFinished']
        for i in range(len(champ_data['dates'])):
            durl= url[:55]+"match/d"+champ_data['dates'][i]['raw']+'.json'
            data = requests.get(durl,headers=HEADERS,timeout=30).json()
            for i in range(len(data)):
                var_time = data[i]['Time']
                var_loc = data[i]['LocDesc']
                var_desc = data[i]["Desc"]
                home = data[i]['Home']['Desc']
                Away = data[i]['Away']['Desc']
                team = data[i]['IsTeam']
                mtime = data[i]['Time']
                teamA = None
                teamB = None
                if team == False:
                    try:
                        ittf_instance = Ittf(urlfortournement=url,tournment_name = champName,tournment_location=champLocation,
                        tournment_desc=champDesc,isfinished=champFinished,match_desc=var_desc,match_time=mtime,isteam=team,home=home,away=Away)
                        ittf_instance.save()
                    except :
                        raise 
                    finally:
                        time.sleep(50)
                        

                else:
                    teamA = data[i]['Home']['Desc'].replace('/','&')
                    teamB = data[i]['Away']['Desc'].replace('/','&')
                    try:                  
                        ittf_instance = Ittf(urlfortournement=url,tournment_name = champName,tournment_location=champLocation,
                        tournment_desc=champDesc,isfinished=champFinished,match_desc=var_desc,match_time=mtime,isteam=team,home=home,away=Away,teamA=teamA,teamB=teamB)
                        ittf_instance.save()
                    except :
                        raise 
                    finally:
                        time.sleep(50)
#  urlForTournement = models.CharField(max_length=500)
#     tournment_name = models.CharField(max_length=500)
#     tournment_location = models.CharField(max_length=500)
#     tournment_desc = models.CharField(max_length=500)
#     isfinished = models.BooleanField()
#     match_desc = models.CharField(max_length=500)
#     match_time = models.DateTimeField()
#     isteam = models.BooleanField(max_length=500)
#     home = models.CharField(max_length=500)
#     away = models.CharField(max_length=500)
#     teamA = models.CharField(max_length=500,default=None)
#     team2 = models.CharField(max_length=500,default=None)