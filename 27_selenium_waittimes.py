#time taken to load
#like when you open twitter, it takes time to load your profile
# we can use time.sleep()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




s = Service("D:\E_drive\CampusX_DS\extra\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://twitter.com/')

# time.sleep(4)
#waittime method of webdriver


search = driver.find_element_by_xpath(""" **paste xpath """)
search.send_keys('Elon Musk')
search.send_keys(Keys.ENTER)