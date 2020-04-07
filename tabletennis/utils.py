from bs4 import BeautifulSoup
import requests
import re
import time

from .models import Error

HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}

# Scraping the World Tour
def get_world_tour(year):
    world_tour = 'https://www.ittf.com/ittf-world-tour/'
    try:
        page = requests.get(world_tour,headers=HEADERS,timeout=60).text
        soup = BeautifulSoup(page,'html.parser')
        href = soup.find('a',title = re.compile(year)).get('href')
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


# Scraping World Championship
def get_world_champ_comp(year):
    links = []
    url = "https://www.ittf.com/world-championships/"
    try:
        soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=60).text,'html.parser')
        next_page_url = soup.find('a',title = re.compile(year)).get('href')
        links.append(next_page_url)
    except Exception as e:
        print(e)
    
    return links


# Scraping Challenger Series
def get_challange_series(year):
    url = 'https://www.ittf.com/ittf-challenge-series/'
    try:
        soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=60).text,'html.parser')
        next_page_url = soup.find('a',title = re.compile(year)).get('href')
    except Exception as e:
        print(e)
    
    try:
        next_page = BeautifulSoup(requests.get(next_page_url,headers=HEADERS,timeout=60).text,'html.parser')
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


# Scraping WorldCup
def get_worldcup(year):
    main_url = 'https://www.ittf.com/world-cup/'
    links = []
    try:
        page = BeautifulSoup(requests.get(main_url,headers=HEADERS,timeout=60).text,'html.parser')
        men_url = page.find('a',title="Men's World Cup").get('href')
        women_url = page.find('a',title="Women's World Cup").get('href')
        team_url = page.find('a',title="Team World Cup").get('href')
    except Exception as e:
        print(e)
    
    try:
        men_page = BeautifulSoup(requests.get(men_url,headers=HEADERS,timeout=60).text,'html.parser')
        links.append(men_page.find('a',title=re.compile(year)).get('href'))
        time.sleep(10)
        women_page = BeautifulSoup(requests.get(women_url,headers=HEADERS,timeout=60).text,'html.parser')
        links.append(women_page.find('a',title=re.compile(year)).get('href'))
        time.sleep(10)
        team_page = BeautifulSoup(requests.get(team_url,headers=HEADERS,timeout=60).text,'html.parser')
        links.append(team_page.find('a',title=re.compile(year)).get('href'))
    except Exception as e:
        print(e)

    return links


# Getting champ.json file
def get_champ_json(links_list):
    links = []
    for link in links_list:
        try:
            get_link = BeautifulSoup(requests.get(link,headers=HEADERS,timeout=50).text,'html.parser')
            if not(get_link.is_empty_element):
                name = get_link.find('h1',class_="media-heading").text
                key_ = get_link.find('a',text=re.compile('Daily Schedule')).get('href')
                value_ = key_[:55]+"champ.json"
                links.append([name,link,value_])

        except Exception as e:
            error, _ = Error.objects.get_or_create(url=link,error=e,extra_info=name)
    return links


# Getting Data from champ.json
def champ_json(url):
    try:
        r_json = requests.get(url,headers=HEADERS,timeout=60).json()
        time.sleep(10)
    except Exception as e:
        print(e)
    
    if r_json: 
        return r_json
    else:
        try:
            r_json = requests.get(url,headers=HEADERS,timeout=160).json()
            return r_json
        except Exception as e:
            print(e)


