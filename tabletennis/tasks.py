import os
import re
from bs4 import BeautifulSoup
import  requests
from .utils import champ_json
from .models import RawData,Phases,Table,Competition

def scrape():

    u = "https://results.ittf.com/ittf-web-results/html/TTE5013/champ.json"

    
    json_data = champ_json(u)

    champ = json_data['champ']
    # comp = Competition.objects.get_or_create(champ=champ)
    champ_desc = json_data['champDesc']
    is_finished = json_data['isFinished']
    loc = json_data['location']
    raw_data,created = RawData.objects.get_or_create(raw_data=json_data)
    comp = Competition.objects.update_or_create(champ=champ,description=champ_desc,location=loc,
                                        isfinished=is_finished,url=u)
    comp.raw_comp.add(raw_data)
    comp.save()
    for i in json_data['phases']:
        key = i['Key'].replace('-','')
        desc = i['Desc']
        evkey = i['EvKey'].replace('-','')
        ev_type = i['Type']
        phase,created = Phases.objects.get_or_create(key=key,desc=desc,evkey=evkey,phase_type=ev_type)
        comp.phase_comp.add(phase)
        comp.save()
        print(phase)
    for data in json_data['locations']:
        key = data['Key']
        desc = data['Desc']
        table,created = Table.objects.get_or_create(key=key,desc=desc)
        comp.table_comp.add(table)
        comp.save()
        print(table.id)

    # Competition.objects.update_or_create(champ=champ,description=champ_desc,location=loc,
    #                                     isfinished=is_finished,url=u,raw_comp=raw_data, 
    #                                     phase_comp=Phases_list,table_comp=table_list)
