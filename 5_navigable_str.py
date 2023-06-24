#all text is navigbale strings
#everyhitng in black

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')


tag = soup.div.p
print(tag.text)


t = soup.header.div.a.button.span
print(t.text)