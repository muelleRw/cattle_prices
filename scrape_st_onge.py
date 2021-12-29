
from datetime import datetime
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
from urllib.parse import urlparse
import os

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


base = "http://www.stongelivestock.com/"
bad_links = []
#links = pd.read_csv("bad_links.csv").to_dict(orient='records')
i=0
for link in links:
    print(i)
    i += 1
    try:
        sale_report = base + link["link"]
        response = requests.get(sale_report)
        with open('st_onge_pdf/' + os.path.basename(urlparse(link['link']).path), 'wb') as f:
            f.write(response.content)

    except Exception as e:
        bad_links.append(link)
        print(e)
        print(link["link"])