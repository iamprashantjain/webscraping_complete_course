# find_all with tags & attributes
# find all will find all data unlike find function


import requests
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

price = soup.find_all('h4', class_ = 'pull-right price')
for i in price:
    print(i.text.strip())


title = soup.find_all('a',class_="title")
for i in title:
    print(i.text.strip())


desc = soup.find('p', class_="description")
print(desc)

# for i in desc:
#     print(i.text.strip())