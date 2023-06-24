# <head></head> --> contains title of the page
# <body></body> --> rest everything is in body
# head & body are open & close tags

# website structure is devided into mutliple divs
# each div contains other tags like div, a, p, ul, button, navbar, image etc


import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')


#in order to get all div tags
print(soup.div)


#everything in purpule colour is a TAG