from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


s = Service("D:\E_drive\CampusX_DS\extra\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.google.com/search?sxsrf=APwXEdecE99zXyb4jdKL0grNKlIBMhfqJQ:1687769429397&q=pandas&tbm=isch&sa=X&ved=2ahUKEwjb5bSKx-D_AhWNg2MGHZvODtcQ0pQJegQIDBAB&biw=1366&bih=617&dpr=1')
height = driver.execute_script("return document.body.scrollHeight")      #get the scroll height
# print(height)


#scroll to that height
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")