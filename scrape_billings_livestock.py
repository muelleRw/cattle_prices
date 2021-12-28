
from datetime import datetime
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
sale_list = "https://www.billingslivestock.com/Cow_Sales/CS_PastSales.html"

sale_list_page = requests.get(sale_list)
soup = BeautifulSoup(sale_list_page.content, 'html.parser')
#soup = BeautifulSoup(sale_list_page.content, parseOnlyThese=SoupStrainer("td"))

links = []
table = soup.find('table', {"id": "table1"})
a_tags = table.find_all("a")
for tr in a_tags:
    record = {
        "date": tr.text.strip(),
        "link": tr.get('href')
    }
    links.append(record)

df_list = []
base = "https://www.billingslivestock.com/Cow_Sales/"
bad_links = []
#links = pd.read_csv("bad_links.csv").to_dict(orient='records')
i=0
for link in links:
    print(i)
    i += 1
    try:
        sale_report = base + link["link"]
        soup = BeautifulSoup(requests.get(sale_report).content, 'html.parser')
        tables = soup.find_all('table')
        #for table in tables:
        data = []
        for table in tables:#tables[0]
            for row in table.find_all("tr"):
                if len(row) > 0:
                    cols = row.find_all("td")
                    if len(cols) < 6:
                        type = cols[0].text.strip()
                    elif len(cols) == 6:
                        record = {
                            "date": link["date"],
                            "type": type,
                            "owner": cols[0].text.strip(),
                            "location": cols[1].text.strip(),
                            "count": cols[2].text.strip(),
                            "class": cols[3].text.strip(),
                            "weight": cols[4].text.strip(),
                            "price": cols[5].text.strip(),
                            "link": link["link"]
                        }
                        data.append(record)
                        #for col in cols:
                        #    #print(col)
                        #    print(col.text.strip())
                    
        if len(data) == 0:
            raise ValueError("No data to append to df_list")
        df_list.append(pd.DataFrame(data))
    except Exception as e:
        bad_links.append(link)
        print(e)
        print(link["link"])

for link in bad_links:
    print(link['link'])

good_df = pd.concat(df_list)#.to_csv("good_links.csv", index=False)

date = good_df['date'].str[:8].str.split('_', expand=True)
date[0] = date[0].str.zfill(2)
date[1] = date[1].str.zfill(2)
date[2] = date[2].str.zfill(2)
date['date'] = date[0] + '_' + date[1] + '_' + date[2]
import datetime
good_df['date'] = date['date']

good_df['date'] = pd.to_datetime(good_df['date'], format='%m_%d_%y')
good_df["type"] = good_df["type"].str.lower()
good_df["owner"] = good_df["owner"].str.lower()
good_df["location"] = good_df["location"].str.lower()
good_df["class"] = good_df["class"].str.lower()

good_df.to_csv("good_links.csv", index=False)

bad_link_df = pd.DataFrame(bad_links)
bad_link_df.to_csv("bad_links.csv", index=False)
