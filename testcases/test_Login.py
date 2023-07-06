from pytest import Class
from pageobjects.LoginPageObjects import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("http://44.211.158.119/login")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("sonam")
        self.lp.setPassword("radiant")
        self.lp.clickLogin()
        self.act_title=self.driver.title
        self.driver.close()
        assert self.act_title == "Radiant RM8000 Series"

    
    
