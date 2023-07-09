import pytest
from pageobjects.LoginPageObject import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.DashboardPageObject import DashboardPage


class TestRm8k:

    def test_login(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("http://44.211.158.119/login")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setCredantials("sonam","radiant")
        self.act_title=self.driver.title
        self.driver.close()
        assert self.act_title == "Radiant RM8000 Series"

    
    def test_addgrp(self):
        self.ag=DashboardPage(self.driver)
        self.ag.addGrp("abc123")
        self.driver.close()
