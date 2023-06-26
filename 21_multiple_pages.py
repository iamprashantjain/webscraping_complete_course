import requests
from bs4 import BeautifulSoup
import pandas as pd

session = requests.Session()

names = []
prices = []
stars = []
ratings = []
reviews = []

for i in range(1, 11):
    url = f'https://www.flipkart.com/search?q=under+50000+price+mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}'
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find('div', class_='_1YokD2 _3Mn1Gg')

    name = [i.text for i in box.find_all('div', class_='_4rR01T')]
    price = [i.text for i in box.find_all('div', class_='_30jeq3 _1_WHN1')]
    star = [i.text for i in box.find_all('div', class_='_3LWZlK')]
    rating_review = box.find_all('span', class_='_2_R_DZ')

    ratings.extend(i.text.split('&')[0].split('Ratings')[0] for i in rating_review)
    reviews.extend(i.text.split('&')[1].split('Reviews')[0] for i in rating_review)

    names.extend(name)
    prices.extend(price)
    stars.extend(star)

    print(len(names))


df = pd.DataFrame({
    'Product_Name': names,
    'Prices': prices,
    'Star': stars,
    'Ratings': ratings,
    'Reviews': reviews
})

print(df)

df.to_csv('flipkart.csv')