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
       

       
       
       
       
       
       
       