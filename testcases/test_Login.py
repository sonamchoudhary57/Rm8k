import pytest
from pageobjects.LoginPageObject import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRm8k:

    @pytest.mark.skip
    def test_login(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("http://44.211.158.119/login")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setCredantials("sonam","radiant")
        self.act_title=self.driver.title
        self.driver.close()
        assert self.act_title == "Radiant RM8000 Series"

    
    def test_dashboard(self):
        print("dashboard")
    
