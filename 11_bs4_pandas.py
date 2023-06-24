import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

price = soup.find_all('h4', class_ = 'pull-right price')
title = soup.find_all('a',class_="title")
desc = soup.find_all('p', class_="description")
reviews = soup.find_all('p', class_ = 'pull-right')


data = []

for p,t,d,r in zip(price,title,desc,reviews):
    data.append({
        'Title':t.text,
        'Description':d.text,
        'Price':p.text.replace('$',''),
        'Reviews':r.text[:-7]
        
    })

df = pd.DataFrame(data)
print(df)