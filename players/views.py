from django.shortcuts import render,HttpResponse
import xml.etree.ElementTree as ET
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
        c.text = lname+","+fname
        d = ET.SubElement(b,'gender')
        d.text = data1[i][2]
        e = ET.SubElement(b,'dob')
        e.text = data1[i][3]
        if data1[i][5] != None:
            g = ET.SubElement(b,'country',id=str(data1[i][5]))
            cntry = Country.objects.get(pk=data1[i][5])
            g.text = str(cntry)
        if data1[i][4] != None:
            f = ET.SubElement(b,'sport',id=str(data1[i][4]))
            sprt = Sport.objects.get(pk=data1[i][4])
            f.text = str(sprt)
        h = ET.SubElement(b,'created_at')
        h.text = str(data1[i][6])

    res = ET.tostring(a)


    return HttpResponse(res,content_type="application/xml")