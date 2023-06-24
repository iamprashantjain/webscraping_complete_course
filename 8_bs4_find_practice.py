#beautifulsoup find() function
import requests
from bs4 import BeautifulSoup

# url = "https://www.scrapethissite.com/pages/"
# r = requests.get(url)
# soup = BeautifulSoup(r.text,'lxml')


# print(soup.find('h3', class_="page-title").text)
# print(soup.find('p', class_="lead session-desc").text.strip())


# url = "https://toscrape.com/"
# r = requests.get(url)
# soup = BeautifulSoup(r.text,'lxml')


# print(soup.find('p').text)


url = "https://www.scrapethissite.com/lessons/sign-up/"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
print(soup.find('div', class_="col-md-5").text.strip())