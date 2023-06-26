import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.amazon.in/gp/bestsellers/luggage/ref=zg_bs_nav_0"
r = requests.get(url)

while True:
    soup = BeautifulSoup(r.text,'lxml')
    np = soup.find('li', class_ = 'a-last')
    np = np.find('a').get('href')
    cnp = "https://www.amazon.in/" + np

    r = requests.get(cnp)
    soup = BeautifulSoup(r.text,'lxml')