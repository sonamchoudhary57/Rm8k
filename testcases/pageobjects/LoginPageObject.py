from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    #Locators
    txtbox_username_name="username"
    txtbox_password_name="password"
    button_login_xpath="//button[normalize-space()='Submit']"

    #constructor
    def __init__(self,driver):
        self.driver=driver

    #action methods
    def setCredantials(self,username,pwd):
        usernametxt=self.driver.find_element(By.NAME,self.txtbox_username_name)
        usernametxt.send_keys(username)

    # setPassword
        passwordtxt=self.driver.find_element(By.NAME,self.txtbox_password_name)
        passwordtxt.send_keys(pwd)

    #  clickLogin
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()