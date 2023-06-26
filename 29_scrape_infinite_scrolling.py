from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


s = Service("D:\E_drive\CampusX_DS\extra\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.nike.com/in/w/mens-shoes-nik1zy7ok")
time.sleep(5)


while True:
    height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scroll(0,document.body.scrollHeight)")
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
