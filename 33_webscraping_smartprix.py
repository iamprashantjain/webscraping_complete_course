from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


s = Service("D:\E_drive\CampusX_DS\extra\webscraping\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.smartprix.com/mobiles/exclude_global-exclude_out_of_stock-exclude_upcoming-stock")
time.sleep(2)


#already checked so removing
driver.find_element(By.XPATH,"/html/body/div[1]/main/aside/div/div[5]/div[2]/label[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/main/aside/div/div[5]/div[2]/label[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/main/aside/div/div[5]/div[2]/label[4]/span").click()
time.sleep(2)


#adding exclusions again
driver.find_element(By.XPATH,"/html/body/div[1]/main/aside/div/div[5]/div[2]/label[1]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/main/aside/div/div[5]/div[2]/label[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/main/aside/div/div[5]/div[2]/label[4]/span").click()
time.sleep(2)


height = driver.execute_script('return document.body.scrollHeight')
    
while True:
    driver.find_element(By.XPATH,""" /html/body/div[1]/main/div[1]/div[2]/div[3]""").click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')
    
    if new_height == height:
            break
        
    height = new_height

html = driver.page_source 

with open('smartprix.html','w', encoding='utf-8') as f:
      f.write(html)      

#next part      