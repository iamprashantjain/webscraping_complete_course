from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


s = Service("D:\E_drive\CampusX_DS\extra\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

#take screenshot of full page
driver.get('https://www.tutorialsfreak.com/')

# time.sleep(2)
# driver.save_screenshot(r"D:\E_drive\CampusX_DS\extra\webscraping_complete_course\python_files\full_page.png")


#take screenshot of specific element of page
driver.find_element_by_xpath(""" /html/body/div/div[2]/div/section[1]/div/div[1]/div/div/div/div[3]/img """).screenshot(r"D:\E_drive\CampusX_DS\extra\webscraping_complete_course\python_files\s_element.png")