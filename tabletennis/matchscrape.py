from bs4 import BeautifulSoup
import requests
import re
import time

from .utils import get_champ_json
from .models import *
from players.models import *

HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


def tour_info_general(links,type_string,year):

    tour_type = type_string
    
    for link in links:
        print(link)
        tour_list = get_champ_json(link)
        # return from get_champ_json [name,link,json_data,key_,champ,champ_desc,champ_dates,champ_loc,champ_events,champ_phases,is_fin]
        #print(tour_list)
        #RawData Table INSERT
        name = tour_list[0]
        url = tour_list[1]
        rawData = tour_list[2]
        is_fin = tour_list[10]
        raw_data,raw_ = RawData.objects.get_or_create(name=name,url=url,raw_data=rawData,tour_type=tour_type,is_finished=bool(is_fin))

        # Champ general Data
        champ_id = tour_list[4]
        champ_desc = tour_list[5]
        season_name = champ_desc[-1]
        tournament_name = champ_desc[0]
        Npattren = re.compile('\w[A-Za-z]+')
        trn_nam = Npattren.findall(tournament_name)
        trn_name = " "
        trn_name = trn_name.join(trn_nam)
        location = tour_list[7]
        champ_events = tour_list[8]
        champ_Phases = tour_list[9]
        genders = set([champ_events[i]['Key'][0] for i in range(len(tour_list[8]))])
        match_type = set([champ_events[i]['Key'][2] for i in range(len(tour_list[8]))])

        #Date Magic with start and end dates + extracting matches urls
        dates = tour_list[6]
        key_ = tour_list[3]
        matchurls = [(key_[:55]+"match/d"+dates[i]['raw']+".json") for i in range(len(dates))]
        startD = dates[0]['raw']
        endD = dates[-1]['raw']


        sport = Sport.objects.get(pk=10)
        # players.CompetitionType Table INSERT
        comp_type,comptype_ = CompetitionType.objects.get_or_create(name=type_string)

        # players.Season Table INSERT
        season,season_ = Season.objects.get_or_create(snid=year,tsname=season_name)

        # players.Competition INSERT
        competition, comp_ = Competition.objects.get_or_create(trnname= trn_name ,sptid=sport,turid=comp_type,snid=season) 

        # tabletennis.TTCompetition INSERT
        ttcomp, ttcomp_ = TTCompetition.objects.get_or_create(tour_id=champ_id,competition_id=competition,finished=is_fin,gender=genders,
                            m_type=match_type,startdate=startD,enddate=endD)

        # tabletennis.MatchUrls INSERT
        for url in matchurls:
            murls, murls_ = MatchUrl.objects.get_or_create(match_url=url,champ_id=ttcomp)

        # tabletennis.Event INSERT
        for event in champ_events:
            eve, eve_ = Event.objects.get_or_create(champ_events=ttcomp,event_key=event['Key'],event_desc=event['Desc'])

        # tabletennis.Phase INSERT
        for ph in champ_Phases:
            phses, phses_ = Phase.objects.get_or_create(champ_phase=ttcomp,phase_key=ph['Key'],phase_desc=ph['Desc'],
                                                        phase_evkey=ph['EvKey'],phase_type=ph['Type'])
