
from datetime import datetime
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
sale_list = "http://www.stongelivestock.com/index.cfm?show=10&mid=16"

sale_list_page = requests.get(sale_list)
soup = BeautifulSoup(sale_list_page.content, 'html.parser')
#soup = BeautifulSoup(sale_list_page.content, parseOnlyThese=SoupStrainer("td"))
links = []
p_tags = soup.find_all("p")
for p in p_tags:
    a_tags = p.find_all('a')
    for a in a_tags:
        link = a.get('href')
        if link[17] == 'C':
            record = {
                "date": a.text.strip(),
                "link": link
            }
            links.append(record)
