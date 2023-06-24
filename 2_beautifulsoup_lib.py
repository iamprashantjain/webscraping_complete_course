#to parse html or decode html in a structured way from previous step
#we can use beautifulsoup library

import requests
from bs4 import BeautifulSoup


url1 = "https://courses.wscubetech.com/s/store/courses"
r1 = requests.get(url1)       #200 means rqst successful & we can use html of the page
# print(r1)


soup = BeautifulSoup(r1.text,'lxml')
# print(soup)


#use webscraping text sites
url2 = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r2 = requests.get(url2)
soup1 = BeautifulSoup(r2.text,'lxml')
print(soup1)