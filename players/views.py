from django.shortcuts import render,HttpResponse
import xml.etree.ElementTree as ET

from tabletennis.models import *
from .models import *
from django.http import QueryDict
from django.utils import timezone
from datetime import datetime


def PlayerXML(request):
    data = request.GET.dict()
    
    # Validation for ctrname and sprtname filter
    for k,v in data.items():
        if k == "ctrname":
            ctry_id = Country.objects.get(code=v)
            data['country'] = data.pop(k)
            data['country'] = ctry_id
        if k == "sptname":
            sprt_id = Sport.objects.get(code=v)
            data['sport'] = data.pop(k)
            data['sport'] = sprt_id

    # Creating QuerySet using request.GET dict
    q = QueryDict('',mutable=True)
    q.update(data)
    
    data1 = Player.objects.filter(**q.dict()).values_list()

    # XML Generated according to QuerySet
    a = ET.Element('Players',created_at=str(timezone.now()))
    for i in range(len(data1)):
        print(data1[i],"TESTING")
        b = ET.SubElement(a,'player',id=str(data1[i][0]))
        c = ET.SubElement(b,'name')
        f_name = data1[i][1]
        l_name = data1[i][2].strip().lower()
        lname= str(l_name).capitalize()
        fname= str(f_name)
        c.text = lname+","+" "+fname
        d = ET.SubElement(b,'gender')
        d.text = data1[i][3]
        e = ET.SubElement(b,'dob')
        e.text = data1[i][4]
        if data1[i][5] != None:
            g = ET.SubElement(b,'country',id=str(data1[i][6]))
            cntry = Country.objects.get(pk=data1[i][6])
            g.text = str(cntry).capitalize()
        if data1[i][4] != None:
            f = ET.SubElement(b,'sport',id=str(data1[i][5]))
            sprt = Sport.objects.get(pk=data1[i][5])
            f.text = str(sprt)

    res = ET.tostring(a)


    return HttpResponse(res,content_type="application/xml")



def TourXML(request):
    data = request.GET.dict()
    
    argsdict = {}
    season_data = 0
    comp_type = 0
    for k,v in data.items():
        if k == "turid":
            comp_type = CompetitionType.objects.get(id=v)
            argsdict.update({"turid":comp_type})
        if k == "turname":
            comp_type = CompetitionType.objects.get(name=v)
            argsdict.update({"turid":comp_type})
        if k == "snid":
            season_data = Season.objects.get(snid=v)
            argsdict.update({"snid":season_data})
        if k == "tsname":
            season_data = Season.objects.get(tsname=v)
            argsdict.update({"tsname":season_data})
    
    # Creating QuerySet using request.GET dict
    q = QueryDict('',mutable=True)
    q.update(argsdict)
    all_comp = Competition.objects.filter(**q.dict()).values_list()
    
    a = ET.Element('tournaments',created_at=str(timezone.now()))
    
    for i in range(len(all_comp)):
        turid = CompetitionType.objects.get(id=all_comp[i][4])
        sport_id = str(all_comp[i][2])
        country = str(all_comp[i][3])
        tour_id = str(all_comp[i][0])
        tour_name = str(all_comp[i][1])
        season_info = Season.objects.get(id=all_comp[i][5])
        tdates = TTCompetition.objects.get(competition_id=all_comp[i])
        b = ET.SubElement(a,'tournament',turid=str(turid.id),turname=str(turid.name),sptid=sport_id,cntid=country,
                            trnid=tour_id,trnname=tour_name,tsid=str(season_info.id),tsname=str(season_info.tsname),
                                tssd=str(tdates.startdate),tsed=str(tdates.enddate),snid=str(season_info.snid),
                                gen=str(tdates.gender),type=str(tdates.m_type))



    res = ET.tostring(a)

    return HttpResponse(res,content_type="application/xml")    


def StageXML(request):
    data = request.GET.dict()
    argsdict = {}
    season_data = 0
    for k, v in data.items():
        if k == "snid":
            season_data = Season.objects.get(snid=v)
            argsdict.update({"snid": season_data})
        if k == "tsid":
            season_data = Season.objects.get(id=v)
            argsdict.update({"id": season_data})
        if k == "tsname":
            season_data = Season.objects.get(tsname=v)
            argsdict.update({"tsname": season_data})
    
     # Creating QuerySet using request.GET dict
    q = QueryDict('', mutable=True)
    q.update(argsdict)

    phase_data = Phase.objects.filter(**q.dict()).values_list()

    a = ET.Element('stages')
    for i in range(len(phase_data)):
        one_phase = phase_data[i]
        comp_info = Competition.objects.get(competitionid=one_phase[1])
        season_info = Season.objects.get(id=comp_info.snid_id)
        round_name = one_phase[3].split('-')
        event_info = Event.objects.filter(champ_events=one_phase[1],event_key=one_phase[4])
        b = ET.SubElement(a, 'stage', tsid=str(season_info.id), tsname=str(season_info.tsname), drwid=str(event_info[0].id), drwname=str(event_info[0].event_desc), type=str(one_phase[5]), rndid=str(one_phase[0]), rndname=str(round_name[1]))

    res = ET.tostring(a)

    return HttpResponse(res, content_type="application/xml")

def double_player(request):
    data= request.GET.dict()
    all_teams=Team.objects.all()
    a = ET.Element('Teams',created_at=str(timezone.now()))
    for i in range(len(all_teams)):
        one_team=all_teams[i]
        P1_Fname = one_team.player_1.player_key.first_name
        P1_Lname = one_team.player_1.player_key.last_name.lower()
        P2_Fname = one_team.player_2.player_key.first_name
        P2_Lname = one_team.player_2.player_key.last_name
        P1_Lname = P1_Lname.capitalize()
        P2_Lname = P2_Lname.capitalize()
        b = ET.SubElement(a,'Team',id=str(one_team.id),name =P1_Lname +" & "+ P2_Lname )
        c = ET.SubElement(b, 'player1', id=str(one_team.player_1.player_key.id), name=str(P1_Fname +" "+ P1_Lname))
        d = ET.SubElement(b, 'player2', id=str(one_team.player_2.player_key.id), name=str(P2_Fname +" "+ P2_Lname))
        
    res = ET.tostring(a)
    return HttpResponse(res, content_type="application/xml")

def matchXML(request):
    data = request.GET.dict()
    sings = Single.objects.all()
    doubles = Double.objects.all()
    now = datetime.now().replace(microsecond=0)
    time_stamp =str(datetime.timestamp(now)).split('.')
    a = ET.Element('fixtures', timestamp=str(time_stamp[0]), time=str(now))

    for i in range(len(sings)):
        sin = sings[i]
        one_match = Match.objects.get(id=sin.match_id)
        one_phase = Phase.objects.get(id=one_match.phase_id)
        tourn_info = Competition.objects.get(trnid=one_match.tourn_id.competition_id_id)
        round_name = one_phase.phase_desc.split('-')
        season_info = Season.objects.get(id=one_match.tourn_id.competition_id.snid_id)
        event_info = Event.objects.get(id=one_match.event_id)
        match_id = one_match.id
        lastupdate =one_match.updated_at
        H_Fname = sin.home.player_key.first_name
        H_Lname = sin.home.player_key.last_name.lower()
        A_Fname = sin.away.player_key.first_name
        A_Lname = sin.away.player_key.last_name
        H_Lname = H_Lname.capitalize()
        A_Lname = A_Lname.capitalize()
        gend = str(one_phase.phase_key[0:3:2])
        b = ET.SubElement(a, 'fixture', id =str(match_id), last_update=str(lastupdate))
        c = ET.SubElement(b, 'Time')
        c.text = one_match.match_date+" "+one_match.m_time
        d = ET.SubElement(b, 'stage', turid=str(tourn_info.turid.id), turname=str(tourn_info.turid.name), trnid=str(tourn_info.trnid), trnname=str(tourn_info.trnname), tsid=str(season_info.id), tsname=str(season_info.tsname), gen=gend, type=str(one_phase.phase_type), cntid=str(tourn_info.cntid.id), sptid=str(tourn_info.sptid.id), rndid=str(one_phase.id), rndname=str(round_name[1][1::]))
        e = ET.SubElement(b, 'hteam', id=str(sin.home.player_key.id), name=str(H_Fname + ", " + H_Lname))
        f = ET.SubElement(b, 'ateam', id=str(sin.away.player_key.id), name=str(A_Fname + ", " + A_Lname))
    for x in range(len(doubles)):
        dub = doubles[x]
        two_match = Match.objects.get(id=dub.match_id)
        two_phase = Phase.objects.get(id=two_match.phase_id)
        dubtourn_info = Competition.objects.get(trnid=two_match.tourn_id.competition_id_id)
        dubround_name = one_phase.phase_desc.split('-')
        dubseason_info = Season.objects.get(id=two_match.tourn_id.competition_id.snid_id)
        dubevent_info = Event.objects.get(id=two_match.event_id)
        dubmatch_id = two_match.id
        dublastupdate = two_match.updated_at
        HT_ID = dub.home_T.id
        P1HT_ID = dub.home_T.player_1.player_key.id
        P1HT_Fname = dub.home_T.player_1.player_key.first_name
        P1HT_Lname = dub.home_T.player_1.player_key.last_name
        P2HT_ID = dub.home_T.player_2.player_key.id
        P2HT_Fname = dub.home_T.player_2.player_key.first_name
        P2HT_Lname = dub.home_T.player_2.player_key.last_name
        AT_ID = dub.away_T.id
        P1AT_ID = dub.away_T.player_1.player_key.id
        P1AT_Fname = dub.away_T.player_1.player_key.first_name
        P1AT_Lname = dub.away_T.player_1.player_key.last_name
        P2AT_ID = dub.home_T.player_2.player_key.id
        P2AT_Fname = dub.away_T.player_2.player_key.first_name
        P2AT_Lname = dub.away_T.player_2.player_key.last_name
        P1HT_Lname = P1HT_Lname.capitalize()
        P2HT_Lname = P2HT_Lname.capitalize()
        P1AT_Lname = P1AT_Lname.capitalize()
        P2AT_Lname = P2AT_Lname.capitalize()

        dubgend = str(two_phase.phase_key[0:3:2])
        g = ET.SubElement(a, 'fixture', id=str(dubmatch_id),last_update=str(dublastupdate))
        h = ET.SubElement(g, 'Time')
        h.text = two_match.match_date+" "+ two_match.m_time
        j = ET.SubElement(g, 'stage', turid=str(dubtourn_info.turid.id), turname=str(dubtourn_info.turid.name), trnid=str(dubtourn_info.trnid), trnname=str(dubtourn_info.trnname), tsid=str(dubseason_info.id), tsname=str(
            dubseason_info.tsname), gen=dubgend, type=str(two_phase.phase_type), cntid=str(dubtourn_info.cntid.id), sptid=str(dubtourn_info.sptid.id), rndid=str(two_phase.id), rndname=str(dubround_name[1][1::]))
        k = ET.SubElement(g, 'hteam', id=str(HT_ID), name=str(P1HT_Lname +" & "+P2HT_Lname))
        l = ET.SubElement(k, 'player1', id=str(P1HT_ID), name=str(P1HT_Lname+", "+P1HT_Fname))
        m = ET.SubElement(k, 'player2', id=str(P2HT_ID), name=str(P2HT_Lname+", "+P2HT_Fname))
        n = ET.SubElement(g, 'ateam', id=str(AT_ID), name=str(P1AT_Lname +" & "+P2AT_Lname))
        o = ET.SubElement(n, 'player1', id=str(P1AT_ID), name=str(P1AT_Lname+", "+P1AT_Fname))
        p = ET.SubElement(n, 'player1', id=str(P2AT_ID), name=str(P2AT_Lname+", "+P2AT_Fname))
    res = ET.tostring(a)

    return HttpResponse(res, content_type="application/xml")
