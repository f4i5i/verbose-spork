# import requests
# import re
# import time
# from bs4 import BeautifulSoup

# from .models import *


# HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


# def get_match_data():
#     raw_data = MatchRawData.objects.all()
#     for i in range(len(raw_data)):
#         url = raw_data[i].url
#         champ_id = raw_data[i].comp
#         r = raw_data[i].json_data
#         print('-----------------------------------------------')
#         print(url)
#         print('-----------------------------------------------')
#         if r:
#             for j in range(len(r)):
#                 try:
#                     key = r[j]['Key'].replace('-','').split('.')[:-1]
#                     key = '.'.join(key)
#                     key = key.strip()
#                     Desc = r[j]['Desc'].split('-')[:-1]
#                     Desc = '-'.join(Desc)
#                     Desc = Desc.strip()
#                     phase = Phases.objects.get(key=key,desc=Desc)
#                     match = r[j]['Desc'].split('-')[-1]
#                     time_ = r[j]['Time']
#                     loc = r[j]['Loc']
#                     locdesc = r[j]['LocDesc']
#                     table,_ = Table.objects.get_or_create(key=loc,desc=locdesc)
#                     status = int(r[j]['Status'])
#                     venue = r[j]['Venue'].strip()
                    

#                     home = r[j]['Home']['Desc'].strip()
#                     away = r[j]['Away']['Desc'].strip()



#                     isTeam_home = r[j]['Home']['Desc'].find('/')
#                     isTeam_away = r[j]['Away']['Desc'].find('/')
#                     print(phase)
#                     print(home)
#                     print(away)
#                     print(j)
#                     if home != 'BYE' and away != 'BYE':
#                         if isTeam_home.bit_length() > 1 :
#                             players_home = home.split('/')
#                             players_away = away.split('/')

#                             if players_home != [''] and players_away != ['']:

#                                 player1_home = players_home[0]
#                                 player2_home = players_home[1]


#                                 player1_away = players_away[0]
#                                 player2_away = players_away[1]
#                             else:
                        
#                                 player1_home = r[j]['Home']['Members'][0]['Desc']
#                                 player2_home = r[j]['Home']['Members'][1]['Desc']
                            
#                                 player1_away = r[j]['Away']['Members'][0]['Desc']
#                                 player2_away = r[j]['Away']['Members'][1]['Desc']

#                             c_p1_home = r[j]['Home']['Members'][0]['Org']
#                             c_p2_home = r[j]['Home']['Members'][1]['Org']

#                             c_p1_away = r[j]['Away']['Members'][0]['Org']
#                             c_p2_away = r[j]['Away']['Members'][1]['Org']

#                             c_home1 = Country.objects.get(short_name=c_p1_home)
#                             c_home2 = Country.objects.get(short_name=c_p2_home)

#                             c_away1 = Country.objects.get(short_name=c_p1_away)
#                             c_away2 = Country.objects.get(short_name=c_p2_away)

#                             ply1_home,created5 = Player.objects.get_or_create(name=player1_home,org=c_home1)
#                             ply2_home,created6 = Player.objects.get_or_create(name=player2_home,org=c_home2)
#                             print("Home team :",created5,created6)

#                             ply1_away,created_ply1_away = Player.objects.get_or_create(name=player1_away,org=c_away1)
#                             ply2_away,created_ply2_away = Player.objects.get_or_create(name=player2_away,org=c_away2)
#                             print("away team",created_ply1_away,created_ply2_away)
                            

#                             team_home,created_team_home = Team.objects.get_or_create(player1=ply1_home,player2=ply2_home)
#                             team_away,created_team_away = Team.objects.get_or_create(player1=ply1_away,player2=ply2_away)
                
#                             matchteam,created_match = Match.objects.get_or_create(comp=champ_id,team_home=team_home,team_away=team_away,
#                                                                                     match=match,time=time_,venue=venue,phase=phase,
#                                                                                     table=table,status=status)
#                         else:
#                             short_away = r[j]['Away']['Org']

#                             short_home = r[j]['Home']['Org']

#                             c_name_home = Country.objects.get(short_name=short_home)
#                             c_name_away = Country.objects.get(short_name=short_away)
            
#                             player_home,created9 = Player.objects.get_or_create(name=home,org=c_name_home)
#                             player_away,created10 = Player.objects.get_or_create(name=away,org=c_name_away)
                    
                    
#                             matchsingle,created_match = Match.objects.get_or_create(comp=champ_id,home=player_home,away=player_away,
#                                                                                     match=match,time=time_,venue=venue,phase=phase,
#                                                                                     table=table,status=status)

#                     else:
#                         # missing = Missingdata.objects.get_or_create(home=home,away=away,url=url,phase=phase.desc)

#                 except Exception as e:
#                     # issue = MatchIssue(champ=champ_id,phase=phase,url=url,home=home,away=away,Desc=Desc,match=match,error=e)
#                     # issue.save()  
#                     # j = j+1
#         else:
#             print(url)    


def get_match_data():
    pass