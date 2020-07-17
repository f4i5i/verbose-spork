import requests
import re
import time
from bs4 import BeautifulSoup

from .models import *


HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}




def get_match_data():
    
    tt_champ = TTCompetition.objects.all()
    
    for champ in tt_champ:
        match_data = RawMatchData.objects.filter(tt_champ=champ)

        for match in match_data:
                        
            json_data = match.data_json

            for data in json_data:
            
                m_date = data["Time"].split(',')[0]
                match_time= data["RTime"]

                phase = data['Key'].split('.')[:-1]
                phase = ".".join(phase).strip()
                phase_db = Phase.objects.get(champ_phase=champ,phase_key=phase)

                m_number = data['Desc'].split('-')[-1].strip()

                event = data['Key'].split('.')[:2]
                event = ".".join(event)
                event_db = Event.objects.get(champ_events=champ,event_key=event)
                ttComp_db = TTCompetition.objects.get(tour_id=champ)
                venue = data['Venue']
                mf_date = ttComp_db.startdate[:-2] + m_date[4:]

                home = data['Home']['Desc'].strip()
                away = data['Away']['Desc'].strip()

                isTeam_home = data['Home']['Desc'].find('/')
                isTeam_away = data['Away']['Desc'].find('/')
                
                print(champ)
                print(home)
                print(away)
                print(mf_date)
                print(phase)
                print("---------------------------------------")
                if home != 'BYE' and away != 'BYE':
                    try:
                        current_match,match_created_or_not = Match.objects.get_or_create(match_date=mf_date,tourn_id=champ,ppstatus="PLAYED",
                                                            m_time=match_time,venue=venue,m_number=m_number,event=event_db,phase=phase_db)

                    except Exception as e:
                        match_error = MatchScrapingError.objects.get_or_create(error=e,champ=champ,desc="Error While scraping match")
                        print(current_match)
                    if isTeam_home.bit_length() > 1:
                        home_player1 = data['Home']['Members'][0]['Reg']
                        home_player2 = data['Home']['Members'][1]['Reg']
                        
                        h_ply1 = Player.objects.get(player_id=home_player1)
                        h_ply2 = Player.objects.get(player_id=home_player2)

                        away_player1 = data['Away']['Members'][0]['Reg']
                        away_player2 = data['Away']['Members'][1]['Reg']

                        a_ply1 = Player.objects.get(player_id=away_player1)
                        a_ply2 = Player.objects.get(player_id=away_player2)
                        # Double Team
                        try:
                            team_home,team_H_created_or_not = Team.objects.get_or_create(player_1=h_ply1,player_2=h_ply2)
                        except Exception as e:
                            teamH_error = MatchScrapingError.objects.get_or_create(error=e,champ=champ,desc="Error While scraping Team Home")


                        try:
                            team_away,team_A_created_or_not = Team.objects.get_or_create(player_1=a_ply1,player_2=a_ply2)
                        except Exception as e:
                            teamA_error = MatchScrapingError.objects.get_or_create(error=e,champ=champ,desc="Error While scraping Team Away")

                        
                        try:
                            double_match,double_created_or_not = Double.objects.get_or_create(home_T=team_home,away_T=team_away,match=current_match)
                        except Exception as e:
                            double_error = MatchScrapingError.objects.get_or_create(error=e,champ=champ,desc="Error While Creating or Updating Double Team")


                    else:
                        # Single Player
                        home_player = data['Home']['Reg']
                        away_player = data['Away']['Reg']
                        
                        try:
                            h_ply = Player.objects.get(player_id=home_player)
                            a_ply = Player.objects.get(player_id=away_player)

                            try:
                                single,single_created_or_not = Single.objects.get_or_create(home=h_ply,away=a_ply,match=current_match)
                            except Exception as e:
                                single_error = MatchScrapingError.objects.get_or_create(error=e,champ=champ,desc="Error While Single match create or update")


                        except Exception as e:
                            print("Player Not found")

                      
                # else:
                #     try:
                #         pass
                #     except Exception as e:
                #         missing_data = MatchScrapingError.objects.get_or_create(error=e,champ=champ,desc="The match is missing a player/team")
