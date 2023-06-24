import requests
from bs4 import BeautifulSoup
import pandas as pd


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
url = "https://www.iplt20.com/auction/2022"
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

print(r)

#all tables starts with table tag
table = soup.find('table', class_ ="ih-td-tab auction-tbl").text
header = soup.find('tr', class_ = 'ih-pt-tbl')

tbody = soup.find('tbody', id='pointsdata')
tr_elements = tbody.find_all('tr')

row_data_list = []

for tr in tr_elements:
    row_data = {}
    row_data['team_name'] = tr.find('h2', class_='ih-pt-cont').text
    row_data['funds_remaining'] = tr.find_all('td')[1].text
    row_data['matches_played'] = tr.find_all('td')[2].text
    row_data['total_points'] = tr.find_all('td')[3].text
    row_data_list.append(row_data)        


df = pd.DataFrame(row_data_list)
print(df)