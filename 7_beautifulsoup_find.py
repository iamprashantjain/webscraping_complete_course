#beautifulsoup find() function
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

print(soup.find('div', class_ = 'col-sm-4 col-lg-4 col-md-4'))

print(soup.find('h4', class_ = 'pull-right price').text)
print(soup.find('a',class_="title").text)
print(soup.find('p', class_="description").text)
print(soup.find('p', class_="pull-right").text)


#find function is only limited to 1st div tag, 1st h4 tag or any other tag, it will only
#extract 1st tag data