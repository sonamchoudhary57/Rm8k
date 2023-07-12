from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
# driver = webdriver.Chrome() 

def cookies(driver):
    cookies = [
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'express:sess.sig', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'h_HT6r8qxwGGxiCSYY0cVJj0UZ8'},
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'express:sess', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJ1c2VyIjp7Il9pZCI6IjY0YWQxNzg3MzM0MWU1MTliYTIzZGY3MSIsInJvbGUiOiJhZG1pbiIsInVzZXJuYW1lIjoic29uYW0ifX0='},    
        {'domain': '44.211.158.119', 'expiry': 1723537973, 'httpOnly': True, 'name': 'token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNvbmFtIiwiaWF0IjoxNjg5MTQyOTE1fQ.VcUdcDSoGUI9FJSVyLAfsK3ztHE6AovlVxeEPR64zBU'}
    ]
    for x in cookies:
        driver.add_cookie(x)
    
    Localstoragedata = [
        {'deviceId':'64ad1a32f34c9319ba73fda2'},
        {'validateLicense':'true'},
        {'exp'	:'2023-07-13T06:21:55.651Z'},	
        {'user_info':'{"user_id":"64ad17873341e519ba23df71","username":"sonam","role":"admin"}'},
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
