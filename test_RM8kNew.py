from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setcookies import Login, cookies
import pytest
driver = webdriver.Chrome()

@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.get("http://44.211.158.119/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    cookies(driver)
    # Login(driver)
    yield driver

@pytest.mark.skip
def test_addgroup(setup):
    time.sleep(5)
    addgrp=setup.find_element(By.XPATH,"//i[@title='Add Group']")
    addgrp.click()

    setup.find_element(By.NAME,"name").send_keys("G6135")
    setup.find_element(By.XPATH,"//button[normalize-space()='Select Parent Group']").click()
    setup.find_element(By.XPATH,"//a[normalize-space()='root']").click()
    setup.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
    elements = setup.find_elements(By.CLASS_NAME,"rct-icon rct-icon-uncheck")
    for x in elements:
        print(x)
        x.click()
    assert setup.find_element(By.XPATH,"//span[contains(text(),'G6135')]").is_displayed()


#ADD DEVICE
@pytest.mark.skip
def test_addDevice(setup):

    setup.find_element(By.XPATH,"//button[@title='Add Device']").click()
    add_device=setup.find_element(By.ID,"sourceAddress")
    add_device.send_keys("http://50.239.254.200")
    setup.find_element(By.XPATH,"//button[normalize-space()='Select Group']").click()
    setup.find_element(By.XPATH,"//a[normalize-space()='root']").click()
    setup.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
    assert setup.find_element(By.XPATH,"//span[contains(text(),'RM1121XD(50.239.254.200)')]").is_displayed()

    time.sleep(3)



#UPdate Funtionality
@pytest.mark.skip
def test_updateFunctionality(setup):

    checkboxes = setup.find_elements(By.XPATH, "//span[contains(@class, 'rct-icon-uncheck')]")
    checkboxes[len(checkboxes)-1].click()

    setup.find_element(By.XPATH,"//button[@title='Update Checked Device']").click()
    setup.find_element(By.XPATH,"//button[normalize-space()='Configure RemoteControls']").click()
    time.sleep(1)
    remotePort = setup.find_elements(By.TAG_NAME, "legend")
    remotePort[3].click()
    time.sleep(5)
    # if action == 'save':
    setup.find_element(By.XPATH,"//button[@class='btn-fill btn btn-dark']").click()
#     else:
# #  cancel update devicebtn-fill btn btn-dark
#         setup.find_element(By.XPATH,"//button[@class='btn-fill btn btn-primary']").click()
#         setup.find_element(By.XPATH,"//button[normalize-space()='Cancel']").click()
#     time.sleep(5)


#Opening player 
@pytest.mark.skip
def test_openPlayer(setup):
    setup.find_element(By.XPATH,"//span[contains(text(),'RM1121XD(50.239.254.195)')]").click()
    setup.find_element(By.XPATH,"//span[contains(text(),'RM1121XD(50.239.254.200)')]").click()
    setup.find_element(By.XPATH,"//button[@title='Setting']").click()
    selectinput=Select(setup.find_element(By.ID,"inputPort"))
    time.sleep(5)
    selectinput.select_by_visible_text("Input Port 3")
    time.sleep(5)
    setup.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()
    time.sleep(10)
    setup.find_element(By.XPATH,"//span[normalize-space()='×']").click()
    setup.find_element(By.XPATH,"//button[@class='btn btn-danger player_cut btn btn-primary']").click()
    time.sleep(5)


#Delete funtionality 
@pytest.mark.skip
def test_deleteFunctionality(setup):

    checkboxes = setup.find_elements(By.XPATH, "//span[contains(@class,'btn btn-danger')]")
    checkboxes[len(checkboxes)-1].click()
    time.sleep(5)

    delete=setup.find_element(By.XPATH,"//i[@title='Delete Checked Device']").click()
    time.sleep(5)
    delete=setup.switch_to.alert
    print(delete.text)
    delete.accept()

    time.sleep(5)
 


@pytest.mark.skip
def test_createRecording(self,setup):
   
    self.driver.find_element(By.XPATH,"//a[normalize-space()='RECORDINGS']").click()
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Create Event']").click()
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Select Device']").click()
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Cancel Selection']").click()
    time.sleep(5)
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Select Device']").click()

    #select device
    time.sleep(20)
    device=self.driver.find_element(By.ID,"649bd0c47ab3c401e4b3b495")
    device.click()
    # print(device.is_selected()) 

    self.driver.find_element(By.XPATH,"//button[normalize-space()='Select this Device for the Event']").click()
    #Enter channel name
    self.driver.find_element(By.ID,"channel").send_keys("asdf")

    # Enter event title
    self.driver.find_element(By.ID,"eventName").send_keys("asdsfdsef")
    selectmode=Select(self.driver.find_element(By.XPATH,"//select[@id='sourceMode']"))
    selectmode.select_by_visible_text("Scheduled Recording")
    time.sleep(2)

    #print all the dropdown options
    alloptions=selectmode.options

    input_elements = self.driver.find_elements(By.XPATH,'//input[@class="form-control"]')
    input_elements[3].click()

    nextButton = self.driver.find_elements(By.XPATH,'//th[@class="rdtNext"]//span')
    nextButton[0].click()

    date_element = self.driver.find_element(By.XPATH, '//td[text()="10"]')
    time.sleep(2)

    # Click on the date element
    date_element.click()


    input_elements[5].click()
    input_elements[4].click()

    timeButton = self.driver.find_elements(By.XPATH,'//span[@class="rdtBtn"]')

    timeButton[0].click()
    timeButton[2].click()

    time.sleep(5)

    input_elements[5].click()
    timeButton[4].click()
    timeButton[4].click()

    timeButton[6].click()
    time.sleep(5)
    
    #save 
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
    time.sleep(5)

@pytest.mark.skip
def test_deleteevents(self,setup):
    
    self.driver.find_element(By.XPATH,"//a[normalize-space()='RECORDINGS']").click()
    self.driver.find_element(By.XPATH,"//table[@class='table table-condensed table-hover filterable-table']//thead//tr//th//input[@aria-label='option 1']").click()
    delete=self.driver.find_element(By.XPATH,"//button[normalize-space()='Delete Event(s)']").click()
    time.sleep(5)
    delete=self.driver.switch_to.alert
    print(delete.text)
    delete.accept()


@pytest.mark.skip
def test_adduser(setup):
    setup.find_element(By.LINK_TEXT,"SETTINGS").click()
    setup.find_element(By.ID,"left-tabs-example-tab-users").click()
    setup.find_element(By.XPATH,"//button[normalize-space()='ADD NEW']").click()
    setup.find_element(By.NAME,"Musername").send_keys("sonam123")
    time.sleep(5)
    usertype=Select(setup.find_element(By.ID,"MuserType"))
    time.sleep(5)
    usertype.select_by_visible_text("Admin")
    setup.find_element(By.ID,"mpassword").send_keys("sonam123")
    setup.find_element(By.XPATH,"//button[@class='btn-fill btn btn-primary']").click()
    time.sleep(10)

# def test_edituser(setup):
#      setup.find_element(By.XPATH,"").click()
#      setup.find_element(By.NAME,"Musername").send_keys("sonam12345")
#      setup.find_element(By.XPATH,"//button[@class='btn-fill btn btn-primary']").click()
#      time.sleep(10)

def test_deleteuser(setup):
    setup.find_element(By.LINK_TEXT,"SETTINGS").click()
    setup.find_element(By.ID,"left-tabs-example-tab-users").click()
    deletes=setup.find_element(By.XPATH,"//button[@class='btn btn-danger']")
    deletes[1].click()
    time.sleep(5)
    delete=setup.switch_to.alert
    print(delete.text)
    delete.accept()


  
    
 

# cookies(driver)
time.sleep(3)


