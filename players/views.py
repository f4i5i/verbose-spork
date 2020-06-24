from django.shortcuts import render,HttpResponse
import xml.etree.ElementTree as ET

from tabletennis.models import *
from .models import *
from django.http import QueryDict
from django.utils import timezone


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
    print(data1)

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
    phase_data = Phase.objects.all()

    a = ET.Element('stages')
    for i in range(len(phase_data)):
        one_phase = phase_data[i]
        season_info = Season.objects.get(tsname=one_phase.champ_phase.competition_id.snid)
        round_name = one_phase.phase_desc.split('-')
        event_info = Event.objects.filter(champ_events=one_phase.champ_phase,event_key=one_phase.phase_evkey)
        # phase_info = Phase.objects.all().filter(champ_phase=one_event.champ_events)
        b = ET.SubElement(a, 'stage', tsid=str(season_info.id), tsname=str(season_info.tsname), drwid=str(event_info[0].id), drwname=str(event_info[0].event_desc), type=str(one_phase.phase_type), rndid=str(one_phase.id), rndname=str(round_name[1]))

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
        # P1_Fname = " "
        # P1_Fname = P1_Fname.join(P1_name[1:])
        P1_Lname = P1_Lname.capitalize()
        # P1_Fname = P1_Fname.capitalize()
        # P2_Fname = " "
        # P2_Fname = P2_Fname.join(P1_name[1:])
        # P2_Fname = P2_Fname.capitalize()
        P2_Lname = P2_Lname.capitalize()
        b = ET.SubElement(a,'Team',id=str(one_team.id),name =P1_Lname +" & "+ P2_Lname )
        c = ET.SubElement(b, 'player1', id=str(one_team.player_1.player_key.id), name=str(P1_Fname +" "+ P1_Lname))
        d = ET.SubElement(b, 'player2', id=str(one_team.player_2.player_key.id), name=str(P2_Fname +" "+ P2_Lname))
        
    res = ET.tostring(a)
    return HttpResponse(res, content_type="application/xml")



def Match(request):
    pass
