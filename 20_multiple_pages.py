import requests
from bs4 import BeautifulSoup
import pandas as pd



names = []
prices = []
descs = []
stars = []
ratings = []
reviews = []


for i in range(1,2):

    url = f'https://www.flipkart.com/search?q=under+50000+price+mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    box = soup.find('div', class_ = '_1YokD2 _3Mn1Gg')


    name = box.find_all('div', class_ = '_4rR01T')
    for i in name:
        n = i.text
        names.append(n)


    price = box.find_all('div', class_ = '_30jeq3 _1_WHN1')
    for i in price:
        n = i.text
        prices.append(n)

    # desc = box.find('ul', class_ = '_1xgFaf')
    # for i in desc:
    #     n = i.text
    #     descs.append(n)

    star = box.find_all('div', class_ = '_3LWZlK')
    for i in star:
        n = i.text
        stars.append(n)


    rating_review = box.find_all('span', class_ = '_2_R_DZ')
    for i in rating_review:
        ratings.append(i.text.split('&')[0].split('Ratings')[0])
        

    for i in rating_review:
        reviews.append(i.text.split('&')[1].split('Reviews')[0])



df = pd.DataFrame({
        'Product_Name':names,
        'Prices':prices,
        'Star':stars,
        'Ratings':ratings,
        'Reviews':reviews
        })


df.to_csv('flipkart.csv')

