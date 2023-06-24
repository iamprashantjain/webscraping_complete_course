import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')
print(boxes)

print(len(boxes))

box = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[3]
print(box)


name = box.find('a').text
print(name)

desc = box.find('p', class_="description").text
print(desc)


price = box.find('h4',class_ = 'pull-right price').text
print(price)


sidemenu = soup.find('div', class_ = 'col-md-3 sidebar').text.strip()
print(sidemenu)


sidemenu = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]
name = soup.find('li', class_= 'active').text
print(name)



