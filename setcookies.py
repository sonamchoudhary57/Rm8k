from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
# driver = webdriver.Chrome() 

def cookies(driver):
    cookies = [
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'express:sess.sig', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 's3IsPCGRnnb1eTQ-FoshNTv_ZTI'},
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'express:sess', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJ1c2VyIjp7Il9pZCI6IjY0YWI5YzgwNGE1ZTE5OTllMjQ4NTliYiIsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoic29uYW0ifX0='},    
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNvbmFtIiwiaWF0IjoxNjg4OTc4NTE5fQ.05MaLmKGk9QLhOquMfG0BI8Jyw5i8Y_WE7ne9-cHe6k'}
    ]
    for x in cookies:
        driver.add_cookie(x)
    
    Localstoragedata = [
        {'deviceId':'64a7f30a8a6ab656aaef0d88'},
        {'validateLicense':'true'},
        {'exp'	:'2023-07-11T08:41:59.510Z'},	
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
