import requests
from bs4 import BeautifulSoup
import pandas as pd


for i in range(2, 100):
    url = f"https://www.flipkart.com/search?q=under+50000+price+mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}"
    r = requests.get(url)

    # Check if the link is valid
    if r.status_code == 200:
        try:
            soup = BeautifulSoup(r.text, 'lxml')
            np = soup.find('a', class_='_1LKTO3')['href']
            cnp = "https://www.flipkart.com" + np
            print(cnp)
        except Exception as e:
            print(e)
            break