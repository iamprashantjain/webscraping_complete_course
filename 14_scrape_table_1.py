import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://ticker.finology.in/"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, 'lxml')

#all tables starts with table tag
table = soup.find('table', class_ = 'table table-sm table-hover screenertable')
# print(table.text)

headers = table.find_all('th')
titles = []

for i in headers:
    titles.append(i.text)

# print(titles)    


#asign header as df column names

df = pd.DataFrame(columns=titles)
# print(df)


rows = table.find_all('tr')
for i in rows[1:]:
    print(i.text)



rows = table.find_all('tr')
for i in rows[1:]:
    data = i.find_all('td')
    row = [tr.text for tr in data]
    # print(row)
    l = len(df)
    df.loc[l] = row


df['Company'] = df['Company'].str.replace('\n', '')
df['PriceRs.'] = df['PriceRs.'].str.replace('\n', '')
df['Day HighRs.'] = df['Day HighRs.'].str.replace('\n', '')

print(df)