import requests
import re
import time
from bs4 import BeautifulSoup

from .models import Phases,Competition,Table,Country,MatchRawData,Player,Match,Team,Missingdata,MatchIssue

HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


def get_match_urls():
    comp = Competition.objects.all()
    var = {}
    for i in range(len(comp)):
        dates = comp[i].compdates.split('},')
        url = comp[i].url
        comp_id= comp[i].champ 
        obj = Competition.objects.get(champ=comp_id)
        for i in range(len(dates)):
            temp = dates[i].replace("'","").split(',')[0].split(":")[1].strip()
            new_url = url[:55]+"match/d"+temp+".json"
            r = requests.get(new_url,headers=HEADERS,timeout=60).json()
            if r:
                raw_data,created = MatchRawData.objects.get_or_create(url=new_url,json_data=r,comp=obj)
                print(raw_data)
                time.sleep(5)
            else:
                print(new_url)

def get_players():
    pass


def get_country():
    link = "https://results.ittf.link/index.php?option=com_fabrik&view=list&listid=37&Itemid=154&resetfilters=0&clearordering=0&clearfilters=0&limitstart37=0"
    link1 = link[:144]+"50"
    link2 = link[:144]+"100"
    link3 = link[:144]+"150"
    link4 = link[:144]+"200"
    try:
        r = requests.get(link,headers=HEADERS,timeout=160).text
        print(r)
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
            c_name = Country.objects.get_or_create(name=l_name,short_name=s_name)


def get_match_data():
    raw_data = MatchRawData.objects.all()
    for i in range(len(raw_data)):
        url = raw_data[i].url
        champ_id = raw_data[i].comp
        r = raw_data[i].json_data
        print('-----------------------------------------------')
        print(url)
        print('-----------------------------------------------')
        if r:
            for j in range(len(r)):
                try:
                    key = r[j]['Key'].replace('-','').split('.')[:-1]
                    key = '.'.join(key)
                    key = key.strip()
                    Desc = r[j]['Desc'].split('-')[:-1]
                    Desc = '-'.join(Desc)
                    Desc = Desc.strip()
                    phase = Phases.objects.get(key=key,desc=Desc)
                    match = r[j]['Desc'].split('-')[-1]
                    time_ = r[j]['Time']
                    loc = r[j]['Loc']
                    locdesc = r[j]['LocDesc']
                    table,_ = Table.objects.get_or_create(key=loc,desc=locdesc)
                    status = int(r[j]['Status'])
                    venue = r[j]['Venue'].strip()
                    

                    home = r[j]['Home']['Desc'].strip()
                    away = r[j]['Away']['Desc'].strip()



                    isTeam_home = r[j]['Home']['Desc'].find('/')
                    isTeam_away = r[j]['Away']['Desc'].find('/')
                    print(phase)
                    print(home)
                    print(away)
                    print(j)
                    if home != 'BYE' and away != 'BYE':
                        if isTeam_home.bit_length() > 1 :
                            players_home = home.split('/')
                            players_away = away.split('/')

                            if players_home != [''] and players_away != ['']:

                                player1_home = players_home[0]
                                player2_home = players_home[1]


                                player1_away = players_away[0]
                                player2_away = players_away[1]
                            else:
                        
                                player1_home = r[j]['Home']['Members'][0]['Desc']
                                player2_home = r[j]['Home']['Members'][1]['Desc']
                            
                                player1_away = r[j]['Away']['Members'][0]['Desc']
                                player2_away = r[j]['Away']['Members'][1]['Desc']

                            c_p1_home = r[j]['Home']['Members'][0]['Org']
                            c_p2_home = r[j]['Home']['Members'][1]['Org']

                            c_p1_away = r[j]['Away']['Members'][0]['Org']
                            c_p2_away = r[j]['Away']['Members'][1]['Org']

                            c_home1 = Country.objects.get(short_name=c_p1_home)
                            c_home2 = Country.objects.get(short_name=c_p2_home)

                            c_away1 = Country.objects.get(short_name=c_p1_away)
                            c_away2 = Country.objects.get(short_name=c_p2_away)

                            ply1_home,created5 = Player.objects.get_or_create(name=player1_home,org=c_home1)
                            ply2_home,created6 = Player.objects.get_or_create(name=player2_home,org=c_home2)
                            print("Home team :",created5,created6)

                            ply1_away,created_ply1_away = Player.objects.get_or_create(name=player1_away,org=c_away1)
                            ply2_away,created_ply2_away = Player.objects.get_or_create(name=player2_away,org=c_away2)
                            print("away team",created_ply1_away,created_ply2_away)
                            

                            team_home,created_team_home = Team.objects.get_or_create(player1=ply1_home,player2=ply2_home)
                            team_away,created_team_away = Team.objects.get_or_create(player1=ply1_away,player2=ply2_away)
                
                            matchteam,created_match = Match.objects.get_or_create(comp=champ_id,team_home=team_home,team_away=team_away,
                                                                                    match=match,time=time_,venue=venue,phase=phase,
                                                                                    table=table,status=status)
                        else:
                            short_away = r[j]['Away']['Org']

                            short_home = r[j]['Home']['Org']

                            c_name_home = Country.objects.get(short_name=short_home)
                            c_name_away = Country.objects.get(short_name=short_away)
            
                            player_home,created9 = Player.objects.get_or_create(name=home,org=c_name_home)
                            player_away,created10 = Player.objects.get_or_create(name=away,org=c_name_away)
                    
                    
                            matchsingle,created_match = Match.objects.get_or_create(comp=champ_id,home=player_home,away=player_away,
                                                                                    match=match,time=time_,venue=venue,phase=phase,
                                                                                    table=table,status=status)

                    else:
                        missing = Missingdata.objects.get_or_create(home=home,away=away,url=url,phase=phase.desc)

                except Exception as e:
                    issue = MatchIssue(champ=champ_id,phase=phase,url=url,home=home,away=away,Desc=Desc,match=match,error=e)
                    issue.save()  
                    j = j+1
        else:
            print(url)    




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
            p_name = tds[p].text.strip()
            p_org = asc[p].text.strip()
            p_gen = gen[p].text.strip()
            p_dob = dob[p].text.strip()
            p_act = active[p].text.strip()

            p_country, _ = Country.objects.get_or_create(short_name=p_org)
            ply,created = Player.objects.get_or_create(player_id= p_id,name= p_name,org= p_country,gender= p_gen,dob= p_dob,activity= p_act)
