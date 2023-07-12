from selenium.webdriver.support import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from setcookies import Login, cookies



driver = webdriver.Chrome()
driver.get("http://44.211.158.119/login")
driver.implicitly_wait(10)
# call
Login(driver)
time.sleep(10)

cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)