from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


s = Service("D:\E_drive\CampusX_DS\extra\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
search = driver.find_element_by_xpath(""" /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea """)
search.send_keys("House of Dragons")
search.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath(""" /html/body/div[6]/div/div[13]/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[5]/div/div/div/div/div/div[1]/div/a/h3 """).click()
time.sleep(2)
driver.save_screenshot(r"D:\E_drive\CampusX_DS\extra\webscraping_complete_course\python_files\hbo.png")