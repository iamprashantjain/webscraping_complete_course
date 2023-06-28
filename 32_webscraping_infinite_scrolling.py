from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# create a new Chrome driver instance
s = Service("D:\E_drive\CampusX_DS\extra\webscraping\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)

try:
    # set an implicit wait time of 10 seconds
    driver.implicitly_wait(10)
    
    # open specific page
    driver.get('https://www.ajio.com/men-backpacks/c/830201001')

    # scroll to the bottom of the page
    height = driver.execute_script('return document.body.scrollHeight')
    
    while True:
        driver.execute_script(f'window.scrollTo(0,{height})')
        time.sleep(2)
        
        new_height = driver.execute_script('return document.body.scrollHeight')
        
        if new_height == height:
            break
        
        height = new_height
    
    
    #saving complete html in a file
    html = driver.page_source
    
    with open('ajio.html','w',encoding='utf-8') as f:
        f.write(html)

    #to avoid browser closing
    #breakpoint()
    
    



except Exception as e:
    print(e)