import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture

def setup():

    driver = webdriver.Chrome()
    
    return driver