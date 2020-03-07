import os
import requests
from bs4 import BeautifulSoup
import re
import time
from .models import Scrapeable, NotScraped



HEADERS =  {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


def get_ittf_url(url):
    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=60).text,'html.parser')
    content_div = soup.find('div',class_="content page-content" )
    div = content_div.find_all('a', href=True)
    href_list = []
    for a in div:
        href_list.append(a.get('href'))
        print("Link is added to list {}".format(a))
    return href_list

def filter_list(url_list):
    url_list = url_list
    not_included = ['Junior','junior','Para','para','Cadet','cadet','Under-21','U-21','u-21','u 21','U 21','pdf','under-21']
    for word in not_included:
        for url in url_list:
            if word in url:
                print("This link {} is removed from list because of {}".format(url,word))
                url_list.remove(url)
    return url_list

def get_daily_schedule(clean_url_list):
    url_list = []
    url_removed = []
    # t0 = time.time()    
    for url in clean_url_list:
        soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=50).text,'html.parser')
        link = soup.find('a',text=re.compile('Daily Schedule'))
        if link != None:
            url_list.append(link.get('href'))
            var = link.get('href')
            # response_delay = time.time() - t0
            scrape = Scrapeable.objects.get_or_create(urlfortour=var)
            print(scrape)
            time.sleep(10)
        else:
            url_removed.append(url)
            notscraped = NotScraped.objects.get_or_create(urlfornotscraped=url)
            print(notscraped)
            # response_delay = time.time() - t0
            time.sleep(10)
    
    return url_list,url_removed









# # https://results.ittf.com/ittf-web-results/html/TTE5019/champ.json
# def get_data(url_list):
#     # durl = []
#     for url in url_list:
#         new_url = url[:55]+"champ.json"
#         print(new_url)
#         champ_data = requests.get(new_url,headers=HEADERS,timeout=30).json()
#         champDesc = champ_data['champDesc']
#         champLocation = champ_data['location']
#         champFinished = champ_data['isFinished']
#         for i in range(len(champ_data['dates'])):
#             durl= url[:55]+"match/d"+champ_data['dates'][i]['raw']+'.json'
#             data = requests.get(durl,headers=HEADERS,timeout=30).json()
#             for i in range(len(data)):
#                 var_time = data[i]['Time']
#                 var_loc = data[i]['LocDesc']
#                 var_desc = data[i]["Desc"]
#                 home = data[i]['Home']['Desc']
#                 Away = data[i]['Away']['Desc']
#                 team = data[i]['IsTeam']
#                 if team == False:
#                     try:
#                         ittf_instance = IttfTable(url,champLocation,
#                         champDesc,champFinished,var_desc, team,home,Away)
#                         db.session.add(ittf_instance)
#                         db.session.commit()
#                     except :
#                         raise 
#                     finally:
#                         return "Success"
#                 else:
#                     teamA = data[i]['Home']['Desc'].replace('/','&')
#                     teamB = data[i]['Away']['Desc'].replace('/','&')
#                     try:                  
#                         ittf_instance = IttfTable(url,champLocation,
#                         champDesc,champFinished,var_desc, team,home,Away,teamA,teamB)
#                         db.session.add(ittf_instance)
#                         db.session.commit()
#                     except :
#                         raise 
#                     finally:
#                         return "Success"
#      db.session.close_all()           
#     return "Success"
    # return durl,champDesc,champLocation

#    id = Column(Integer,primary_key=True)   
#     urlForTournement = Column(String)
#     location = Column(String)
#     tournementDesc = Column(String)
#     isFinished = Column(Boolean)
#     matchDesc = Column(String)
#     isTeam = Column(Boolean)
#     home = Column(String)
#     away = Column(String)
#     teamA = Column(String,nullable=True)
#     teamB = Column(String,nullable = True)

# def get_results(url_list):
#     for url in url_list:
#         data = requests.get(url,headers=HEADERS,timeout=30).json()
#         for i in range(len(data)):
#             var_time = data[i]['Time']
#             var_loc = data[i]['LocDesc']
#             var_desc = data[i]["Desc"]
#             home = data[i]['Home']['Desc']
#             Away = data[i]['Away']['Desc']
#             print(var_time,var_loc,var_desc,home,Away)


