from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
# driver = webdriver.Chrome() 

def cookies(driver):
    cookies = [
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'express:sess.sig', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 's3IsPCGRnnb1eTQ-FoshNTv_ZTI'},
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'express:sess', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJ1c2VyIjp7Il9pZCI6IjY0YWI5YzgwNGE1ZTE5OTllMjQ4NTliYiIsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoic29uYW0ifX0='},    
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNvbmFtIiwiaWF0IjoxNjg4OTg0MzYxfQ.hzomUhw6Nk9HGeA0PVouJxOHadV1IGJO8Bt0MzTmAMI'}
    ]
    for x in cookies:
        driver.add_cookie(x)
    
    Localstoragedata = [
        {'deviceId':'64ab9e0c70f32499e27203a8'},
        {'validateLicense':'true'},
        {'exp'	:'2023-07-11T10:19:21.992Z'},	
        {'user_info':'{"user_id":"64ab9c804a5e1999e24859bb","username":"sonam","role":"admin"}'},
        {'token':'sbvv78dgashjt7632thbhbdas'},	
        {'message':'valid'}	
       ]

    for opt in Localstoragedata:
        for key, value in opt.items():
             driver.execute_script("return localStorage.setItem('" + str(key)+ "', '" + str(value) + "');")
    
    driver.get("http://44.211.158.119/dashboard")
    



def Login(driver):
 driver.find_element(By.NAME,"username").send_keys("sonam1")
 driver.find_element(By.NAME,"password").send_keys("radiant1")
 driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
 time.sleep(5)
