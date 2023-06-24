import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2018"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

table = soup.find('table', class_ = 'ih-td-tab auction-tbl')
header = table.find_all('th')
titles = []

for i in header:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns=titles)

rows = table.find_all('tr')
for i in rows[1:]:
    data = i.find_all('td')
    row = [tr.text for tr in data]

    l = len(df)
    df.loc[l] = row


df['TEAM'] = df['TEAM'].str.replace('\n', '')
df['FUNDS REMAINING'] = df['FUNDS REMAINING'].str.replace('₹','')
print(df)

df.to_csv('ipl.csv')