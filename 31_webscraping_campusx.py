from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("D:\E_drive\CampusX_DS\extra\webscraping\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com")
time.sleep(2)

#opening campusx
driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""").send_keys('Campusx', Keys.ENTER)
time.sleep(2)

#clicking link
driver.find_element(By.XPATH, """//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a""").click()
time.sleep(2)

#click join program
driver.find_element(By.XPATH, """ /html/body/div[5]/div[1]/div[2]/div/div/div/div/span[2]/a """).click()
time.sleep(2)
