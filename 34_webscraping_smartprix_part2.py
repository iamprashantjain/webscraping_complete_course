import re
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

with open('smartprix.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

name = []
price = []
spec = []
sim = []
processor = []
ram = []
battery = []
screen = []
camera = []
card = []
os = []

containers = soup.find_all('div', class_='sm-product has-tag has-features has-actions')
for i in containers:
    name.append(i.find('h2').text)
    price.append(int(i.find('span', class_='price').text.replace('₹', '').replace(',', '')))
    try:
        spec.append(i.find('div', class_='score rank-2-bg').find('b').text)
    except:
        spec.append(np.nan)

    x = i.find('ul', class_='sm-feat specs').find_all('li')

    try:
        sim.append(x[0].text)
    except:
        sim.append(np.nan)

    try:
        processor.append(x[1].text)
    except:
        processor.append(np.nan)

    try:
        data = re.sub(r'[^a-zA-Z0-9\s,]', '', x[2].text)
        ram.append(data)
    except:
        ram.append(np.nan)

    try:
        data = re.sub(r'[^a-zA-Z0-9\s,]', '', x[3].text)
        battery.append(data)
    except:
        battery.append(np.nan)

    try:
        data = re.sub(r'[^a-zA-Z0-9\s,]', '', x[4].text)
        screen.append(data)
    except:
        screen.append(np.nan)

    try:
        data = re.sub(r'[^a-zA-Z0-9\s,]', '', x[5].text)
        camera.append(data)
    except:
        camera.append(np.nan)

    try:
        data = re.sub(r'[^a-zA-Z0-9\s,]', '', x[6].text)
        card.append(data)
    except:
        card.append(np.nan)

    try:
        data = re.sub(r'[^a-zA-Z0-9\s,]', '', x[7].text)
        os.append(data)
    except:
        os.append(np.nan)


print(ram)


df = pd.DataFrame({
    'name': name,
    'price': price,
    'spec_score': spec,
    'sim': sim,
    'processor': processor,
    'ram': ram,
    'battery': battery,
    'screen': screen,
    'camera': camera,
    'card': card,
    'os': os
})

print(df)
df.to_csv('smartprix.csv')