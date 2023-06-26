import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

names = []
prices = []
descs = []
ratings = []

url = 'https://www.airbnb.co.in/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

while True:
    np = soup.find('a', class_='l1ovpqvx c1ytbx3a dir dir-ltr').get('href')
    cnp = "https://www.airbnb.co.in" + np

    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    name = soup.find_all('div', class_='t1jojoys dir dir-ltr')
    for i in name:
        names.append(i.text)

    price = soup.find_all('div', class_='pquyp1l dir dir-ltr')
    for i in price:
        prices.append(i.text.split('night')[0])

    rating = soup.find_all('span', class_='t1a9j9y7 r4a59j5 dir dir-ltr')
    for i in rating:
        ratings.append(i.text.split(' ')[0])

    desc = soup.find_all('span', class_ = 't6mzqp7 dir dir-ltr')
    for i in desc:
        descs.append(i.text)


    # Check if there is a next page
    next_page = soup.find('a', class_='l1ovpqvx c1ytbx3a dir dir-ltr')
    if not next_page:
        break


df = pd.DataFrame({
    'name':names,
    'price':prices,
    'description': descs,
})


print(df)
df.to_csv('airbnb.csv')

