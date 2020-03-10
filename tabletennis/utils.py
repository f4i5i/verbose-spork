from bs4 import BeautifulSoup
import requests
import re
import time


HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}

world_tour = 'https://www.ittf.com/ittf-world-tour/'

def get_world_tour(url):
    try:
        page = requests.get(url,headers=HEADERS,timeout=60).text
        soup = BeautifulSoup(page,'html.parser')
        href = soup.find('a',title='2019 ITTF World Tour').get('href')
    except Exception as e:
        print(e)

    try:
        next_page = BeautifulSoup(requests.get(href,headers=HEADERS,timeout=60).text,'html.parser')
        events = next_page.find('a',title='Events').get('href')
    except Exception as  e:
        print(e)

    try:
        all_events = requests.get(events,headers=HEADERS,timeout=60).text
        events_soup = BeautifulSoup(all_events,'html.parser')
    except Exception as e:
        print(e)
    
    div = events_soup.find('div',class_="content page-content")
    links = div.find_all('a')
    all_links = [i.get('href') for i in links]
    return all_links



def get_champ_json(links_list):
    links = {}
    for link in links_list:
        try:
            get_link = BeautifulSoup(requests.get(link,headers=HEADERS,timeout=50).text,'html.parser')
            if not(get_link.is_empty_element):
                key_ = get_link.find('a',text=re.compile('Daily Schedule')).get('href')
                value_ = key_[:55]+"champ.json"
                links.update({key_:value_})

        except Exception as e:
            print(e)
    return links


def champ_json(url):
    try:
        r_json = requests.get(url,headers=HEADERS,timeout=60).json()
        time.sleep(10)
    except Exception as e:
        print(e)
    
    return r_json

