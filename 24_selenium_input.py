# https://shop.mango.com/in --> ctrl + shift + p
#if you disable JS on the webpage, if its JS driven page everything will be removed from the page
#unlike flipkart which is not driven by JS, even if you disable it, will not change


#in order to obtain data from JS driven pages, we can use selenium
#selenium is a tool to automate web-application


# **** to find any element on webpage by xpath ****
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time



s = Service("D:\E_drive\CampusX_DS\extra\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

#open website
driver.get('https://www.google.com/')
time.sleep(1)

search_box = driver.find_element_by_xpath(""" /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea """)
search_box.send_keys("India News")
search_box.send_keys(Keys.ENTER)
