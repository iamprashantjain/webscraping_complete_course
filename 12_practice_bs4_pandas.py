import requests
from bs4 import BeautifulSoup
import pandas as pd



headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
url = "https://www.smartprix.com/mobiles"
r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,'lxml')
# print(soup.prettify())
# print(soup.find('div', class_ = 'sm-product'))


make = soup.find_all('a', class_ = "name clamp-2")
price = soup.find_all('span', class_ = "price")
spec_score = soup.find_all('div',class_ = 'score rank-2-bg')
desc = soup.find_all('ul',class_ = "sm-feat specs")

data = []

for m,p,s,d in zip(make,price,spec_score,desc):
    data.append({
        'make':make,
        'price':price,
        'spec_score':spec_score,
        'desc':desc
    })

df = pd.DataFrame(data)
print(df.columns)


