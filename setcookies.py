from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
# driver = webdriver.Chrome() 

def cookies(driver):
    cookies = [
        {'domain': '44.211.158.119', 'expiry': 1722667698, 'httpOnly': True, 'name': 'express:sess.sig', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'kleTSvFnElI0Chr4WhPIlnmZreY'},
        {'domain': '44.211.158.119', 'expiry': 1722667698, 'httpOnly': True, 'name': 'express:sess', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJ1c2VyIjp7Il9pZCI6IjY0OTkxZTY4MzA5NjAyMzFjMmI1MmZiOSIsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoic29uYW0ifX0='},
        {'domain': '44.211.158.119', 'expiry': 1722667698, 'httpOnly': True, 'name': 'token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNvbmFtIiwiaWF0IjoxNjg4MTA3Njk2fQ.uiPVOaGDkunK0ZhSeqSjRRVND1_PT8TJrfnd0muUXXg'}
    ]
    for x in cookies:
        driver.add_cookie(x)
    
    Localstoragedata = [
        {'deviceId':'64991ec38de4ae31c23ac3fc'},
        {'validateLicense':'true'},
        {'exp'	:'2023-07-01T06:38:33.087Z'},	
        {'user_info':'{"user_id":"64991e6830960231c2b52fb9","username":"sonam","role":"admin"}'},
        {'token':'sbvv78dgashjt7632thbhbdas'},	
        {'message':'valid'}	
       ]

    for opt in Localstoragedata:
        for key, value in opt.items():
             driver.execute_script("return localStorage.setItem('" + str(key)+ "', '" + str(value) + "');")
    
    driver.get("http://44.211.158.119/dashboard")
    



def Login(driver):
 driver.find_element(By.NAME,"username").send_keys("sonam")
 driver.find_element(By.NAME,"password").send_keys("radiant")
 driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
 time.sleep(5)
