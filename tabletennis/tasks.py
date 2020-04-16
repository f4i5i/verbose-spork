import os
import re
from bs4 import BeautifulSoup
import  requests
import  time
from .utils import *
from .models import *
from .matchscrape import tour_info_general

def scrape():
    world_tour_links = []
    challenge_series_links = []
    world_champ_links = []
    word_cup_links = []
    
    year = "2019"
    
    world_tour = get_world_tour(year)
    [world_tour_links.append(i) for i in world_tour]
    time.sleep(10)
    
    challenger = get_challange_series(year)
    [challenge_series_links.append(i) for i in challenger]
    time.sleep(10)
    
    world_champ = get_world_champ_comp(year)
    [world_champ_links.append(i) for i in world_champ]
    time.sleep(10)
    
    worldcup = get_worldcup(year)
    [word_cup_links.append(i) for i in worldcup]


    tour_info_general(world_tour_links,"World Tour",2019)
    tour_info_general(challenge_series_links,"Challenge Series",2019)
    tour_info_general(world_champ_links,"World Championship",2019)
    tour_info_general(word_cup_links,"World Cup",2019)       
       

       
       
       
       
       
       
       
       
       
        # json_data = champ_json(v)

        # champ = json_data['champ']
        # champ_dates = json_data['dates']
        # # comp = Competition.objects.get_or_create(champ=champ)
        # champ_desc = json_data['champDesc']
        # is_finished = json_data['isFinished']
        # loc = json_data['location']
        # raw_data,created = RawData.objects.get_or_create(raw_data=json_data)
        # comp = Competition.objects.get_or_create(champ=champ,description=champ_desc,location=loc,isfinished=is_finished,url=k,raw_comp=raw_data,compdates=champ_dates)

        # for i in json_data['phases']:
        #     key = i['Key'].replace('-','')
        #     desc = i['Desc']
        #     evkey = i['EvKey'].replace('-','')
        #     ev_type = i['Type']
        #     phase,created = Phases.objects.get_or_create(key=key,desc=desc,evkey=evkey,phase_type=ev_type)
        #     print(phase)
        # for data in json_data['locations']:
        #     key = data['Key']
        #     desc = data['Desc']
        #     table,created = Table.objects.get_or_create(key=key,desc=desc)
        #     print(table.id)


