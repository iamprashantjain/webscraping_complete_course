# https://shop.mango.com/in --> ctrl + shift + p
#if you disable JS on the webpage, if its JS driven page everything will be removed from the page
#unlike flipkart which is not driven by JS, even if you disable it, will not change


#in order to obtain data from JS driven pages, we can use selenium
#selenium is a tool to automate web-application


# **** to find any element on webpage by xpath ****
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time



s = Service("D:\E_drive\CampusX_DS\extra\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

#open website
driver.get('https://tutorialsfreak.com/')


#copy fullxpath
# ****click any button using .click() function ****

time.sleep(2)
driver.find_element_by_xpath(""" /html/body/div/div[2]/div/section[1]/div/div[1]/div/div/div/div[2]/button """).click()
