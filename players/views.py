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

    # XML Generated according to QuerySet
    a = ET.Element('Players',created_at=str(timezone.now()))
    for i in range(len(data1)):
        b = ET.SubElement(a,'player',id=str(data1[i][0]))
        c = ET.SubElement(b,'name')
        name = data1[i][1].strip().lower().split(' ')
        lname = name[-1].capitalize()
        fname = name[0].capitalize()
        c.text = fname+","+" "+lname
        d = ET.SubElement(b,'gender')
        d.text = data1[i][2]
        e = ET.SubElement(b,'dob')
        e.text = data1[i][3]
        if data1[i][5] != None:
            g = ET.SubElement(b,'country',id=str(data1[i][5]))
            cntry = Country.objects.get(pk=data1[i][5])
            g.text = str(cntry).capitalize()
        if data1[i][4] != None:
            f = ET.SubElement(b,'sport',id=str(data1[i][4]))
            sprt = Sport.objects.get(pk=data1[i][4])
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
            argsdict.update({"snid":season_data})
    
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
    seasons_data = Season.objects.get(id=data['tsid'])

    a = ET.Element('stages',,created_at=str(timezone.now()))
    season_id = seasons_data.id
    season_name = seasons_data.tsname
    comp = Competition.objects.get(snid=season_id)
    ttcomp = TTCompetition.objects.get(competition_id=comp)
    pass    