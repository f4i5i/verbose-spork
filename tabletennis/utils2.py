import requests
import re
import time
from bs4 import BeautifulSoup

from .models import *
from players.models import Player,Sport ,Country
from tabletennis.models import Error
from tabletennis.models import Player as TTPlayer

HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


def get_match_urls():
    comp = TTCompetition.objects.all()
    for i in comp:
        if i.finished == True:
            m_urls = MatchUrl.objects.filter(champ_id=i.tour_id)
            for url in m_urls:
                try:
                    j_data = requests.get(url.match_url,headers=HEADERS,timeout=160).json()
                    rawmatch,_ = RawMatchData.objects.get_or_create(tt_champ=i,data_json=j_data)
                    time.sleep(10)
                except Exception as e:
                    print(e)


def get_country():
    link = "https://results.ittf.link/index.php?option=com_fabrik&view=list&listid=37&Itemid=154&resetfilters=0&clearordering=0&clearfilters=0&limitstart37=0"
    link1 = link[:144]+"50"
    link2 = link[:144]+"100"
    link3 = link[:144]+"150"
    link4 = link[:144]+"200"
    try:
        r = requests.get(link,headers=HEADERS,timeout=160).text
        time.sleep(10)
        r1 = requests.get(link1,headers=HEADERS,timeout=160).text
        time.sleep(10)
        r2 = requests.get(link2,headers=HEADERS,timeout=160).text
        time.sleep(10)
        r3 = requests.get(link3,headers=HEADERS,timeout=160).text
        time.sleep(10)
        r4 = requests.get(link4,headers=HEADERS,timeout=160).text
    except Exception as e:
        print(e)
    
    r_list = [r,r1,r2,r3,r4]
    
    for var in r_list:
        soup = BeautifulSoup(var,'html.parser')
        shortName = soup.find_all('td',class_="fab_countries___country fabrik_element fabrik_list_37_group_38")
        longName =  soup.find_all('td',class_="fab_countries___name fabrik_element fabrik_list_37_group_38")
        for i in range(len(shortName)):
            s_name = shortName[i].text.strip()
            l_name = longName[i].text.strip()
            c_name = Country.objects.get_or_create(name=l_name,code=s_name)



def get_player_data():
    url =  "https://results.ittf.link/index.php?option=com_fabrik&view=list&listid=35&Itemid=155&resetfilters=0&clearordering=0&clearfilters=0&limit35=100&limitstart35="

    for i in range(0,37601,100):
        new_str = str(i)
    
        req = requests.get(url+new_str,headers=HEADERS,timeout=60).text
        sp = BeautifulSoup(req,'html.parser')
        ply_id = sp.find_all('td',class_="fab_players___player_id fabrik_element fabrik_list_35_group_36 integer")
        tds = sp.find_all('td',class_="fab_players___name fabrik_element fabrik_list_35_group_36")
        asc = sp.find_all('td', class_ = "fab_players___assoc fabrik_element fabrik_list_35_group_36")
        gen = sp.find_all('td', class_= "fab_players___gender fabrik_element fabrik_list_35_group_36")
        dob = sp.find_all('td',class_ = "fab_players___yob fabrik_element fabrik_list_35_group_36")
        active = sp.find_all('td',class_="fab_players___activity fabrik_element fabrik_list_35_group_36")
        for p in range(len(tds)):
            p_id = ply_id[p].text.strip()

            p_name = tds[p].text.replace("^","").strip()
            p_org = asc[p].text.strip()
            p_gen = gen[p].text.strip()
            p_dob = dob[p].text.strip()
            p_act = active[p].text.strip()

            p_country, _ = Country.objects.get_or_create(code=p_org)
            sport_id = Sport.objects.get(pk=10)
            ply,created = Player.objects.get_or_create(name= p_name,gender= p_gen,dob= p_dob,sport=sport_id,country=p_country)
            tt,boolvalue = TTPlayer.objects.get_or_create(player_id=p_id,player_key=ply)