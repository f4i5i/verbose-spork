import os
import requests
from bs4 import BeautifulSoup
import re
import time
from django_rq import job
from .func import  *
from .models import Tournament,TournamentInfo,Matches,Players
import  django_rq
from datetime import datetime


def scrape():
    HEADERS =  {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}
    url ='https://www.ittf.com/2019-event-calendar/'

    all_urls =get_ittf_url(url)
    f_urls = filter_list(all_urls)
    sub_set = f_urls[13:14]
    sch_list,rv_list = get_daily_schedule(f_urls)
    for url in sch_list:
        tour = Tournament(urlfortournement=url)
        tour.save()
        new_url = url[:55]+"champ.json"
        print(new_url)
        champ_data = requests.get(new_url,headers=HEADERS,timeout=30).json()
        champName = champ_data['champ']
        champStatus = champ_data['status']
        champDates = champ_data['dates']
        champDateDesc = champ_data['datesDesc']
        champDesc = champ_data['champDesc']
        champLocation = champ_data['location']
        champeEvent = [j['Desc'] for j in champ_data['events']]
        champPhases = [j['Desc'] for j in champ_data['phases']]
        champLocations = champ_data['locations']
        champFinished = champ_data['isFinished']
        champ = TournamentInfo(urltournement=tour,champ=champName,
                                status=champStatus,dates=champDates,
                                datesdesc=champDateDesc,champdesc=champDesc,
                                location = champLocation,events=champeEvent,
                                phases=champPhases,locations=champLocations,
                                isfinished=champFinished)
        champ.save()
        
        for i in range(len(champ_data['dates'])):
            durl= url[:55]+"match/d"+champ_data['dates'][i]['raw']+'.json'
            data = requests.get(durl,headers=HEADERS,timeout=30).json()
            for i in range(len(data)):  
                var_key = data[i]['Key']
                var_desc = data[i]['Desc']
                var_time = data[i]['Time']
                var_loc = data[i]['LocDesc']
                var_locdesc = data[i]["LocDesc"]
                var_venue = data[i]['Venue']
                var_rtime = data[i]['RTime']
                var_status = data[i]['Status']
                var_isteam = data[i]['IsTeam']
                var_hascomps = data[i]['HasComps']  
                home_var_reg = data[i]['Home']['Reg']
                home_var_org = data[i]['Home']['Org']
                home_var_orgdesc = data[i]['Home']['OrgDesc']
                away_var_reg = data[i]['Away']['Reg']
                away_var_org = data[i]['Away']['Org']
                away_var_orgdesc = data[i]['Away']['OrgDesc']
                match = Matches(champ=champ,key=var_key,desc=var_desc,
                                time=var_time,loc=var_loc,locdesc=var_locdesc,
                                venue =var_venue,rtime=var_rtime,status = var_status,
                                isteam=var_isteam,hascomps=var_hascomps)
                match.save()
                Home = data[i]['Home']['Desc']
                Away = data[i]['Away']['Desc']
                has_stat = data[i]['HasStats']
                teamA = None
                teamB = None
                if var_isteam == False:
                    try:
                        ply = Players.objects.get_or_create(match=match,home=Home,away=Away,
                                    home_reg=home_var_reg,home_org=home_var_org,home_orgdesc=home_var_orgdesc,
                                    away_reg=away_var_reg,away_org=away_var_org,away_orgdesc=away_var_orgdesc)
                    except:
                        raise
                    finally:
                        time.sleep(5)
                else:
                    teamA = data[i]['Home']['Desc'].replace('/','&')
                    teamB = data[i]['Away']['Desc'].replace('/','&')
                    try:
                        ply = Players.objects.get_or_create(match=match,home=Home,away=Away,
                                    home_reg=home_var_reg,home_org=home_var_org,home_orgdesc=home_var_orgdesc,
                                    away_reg=away_var_reg,away_org=away_var_org,away_orgdesc=away_var_orgdesc,team_a=teamA,team_b=teamB)
                    except :
                        raise 
                    finally:
                        time.sleep(5)
