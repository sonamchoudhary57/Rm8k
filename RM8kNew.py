from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setcookies import cookies

driver = webdriver.Chrome()
driver.get("http://44.211.158.119/login")
driver.implicitly_wait(10)

driver.maximize_window()

def ValidateLogin():
    act_title=driver.title
    exp_title="Radiant RM8000 Series"
    if act_title==exp_title:
        print("Login test passed")
    else:
        print("login test failed")


def AddGroup():
    







    addgrp=driver.find_element(By.XPATH,"//i[@title='Add Group']")
    addgrp.click()

    driver.find_element(By.NAME,"name").send_keys("G6135")
    driver.find_element(By.XPATH,"//button[normalize-space()='Select Parent Group']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='root']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
    elements = driver.find_elements(By.CLASS_NAME,"rct-icon rct-icon-uncheck")

    for x in elements:
        print(x)
        x.click()

 #ADD DEVICE
def AddDevice():
    driver.find_element(By.XPATH,"//button[@title='Add Device']").click()
    add_device=driver.find_element(By.ID,"sourceAddress")
    add_device.send_keys("http://50.239.254.200")
    driver.find_element(By.XPATH,"//button[normalize-space()='Select Group']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='root']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

    time.sleep(3)

#Delete funtionality 
def DeleteFunctionality():
    checkboxes = driver.find_elements(By.XPATH, "//span[contains(@class, 'rct-icon-uncheck')]")
    checkboxes[len(checkboxes)-1].click()
    time.sleep(5)

    delete=driver.find_element(By.XPATH,"//i[@title='Delete Checked Device']").click()
    time.sleep(5)
    delete=driver.switch_to.alert
    print(delete.text)
    delete.accept()

    time.sleep(5)

#UPdate Funtionality
def UpdateFunctionality(action):
    checkboxes = driver.find_elements(By.XPATH, "//span[contains(@class, 'rct-icon-uncheck')]")
    checkboxes[len(checkboxes)-1].click()

    driver.find_element(By.XPATH,"//button[@title='Update Checked Device']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Configure RemoteControls']").click()
    time.sleep(1)
    remotePort = driver.find_elements(By.TAG_NAME, "legend")
    remotePort[3].click()
    time.sleep(5)
    if action == 'save':
        driver.find_element(By.XPATH,"//button[@class='btn-fill btn btn-dark']").click()
    else:
#  cancel update devicebtn-fill btn btn-dark
        driver.find_element(By.XPATH,"//button[@class='btn-fill btn btn-primary']").click()
        driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']").click()
    time.sleep(5)


def createRecording():

    driver.find_element(By.XPATH,"//a[normalize-space()='RECORDINGS']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Create Event']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Select Device']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Cancel Selection']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[normalize-space()='Select Device']").click()

    #select device
    time.sleep(20)
    device=driver.find_element(By.ID,"649bd0c47ab3c401e4b3b495")
    device.click()
    # print(device.is_selected()) 

    driver.find_element(By.XPATH,"//button[normalize-space()='Select this Device for the Event']").click()
    #Enter channel name
    driver.find_element(By.ID,"channel").send_keys("asdf")

    # Enter event title
    driver.find_element(By.ID,"eventName").send_keys("asdsfdsef")
    selectmode=Select(driver.find_element(By.XPATH,"//select[@id='sourceMode']"))
    selectmode.select_by_visible_text("Scheduled Recording")
    time.sleep(2)

    #print all the dropdown options
    alloptions=selectmode.options

    input_elements = driver.find_elements(By.XPATH,'//input[@class="form-control"]')
    input_elements[3].click()

    nextButton = driver.find_elements(By.XPATH,'//th[@class="rdtNext"]//span')
    nextButton[0].click()

    date_element = driver.find_element(By.XPATH, '//td[text()="10"]')
    time.sleep(2)

    # Click on the date element
    date_element.click()


    input_elements[5].click()
    input_elements[4].click()

    timeButton = driver.find_elements(By.XPATH,'//span[@class="rdtBtn"]')

    timeButton[0].click()
    timeButton[2].click()

    time.sleep(5)

    input_elements[5].click()
    timeButton[4].click()
    timeButton[4].click()

    timeButton[6].click()
    time.sleep(5)
    
    #save 
    driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
    time.sleep(5)


def deleteevents():
    driver.find_element(By.XPATH,"//a[normalize-space()='RECORDINGS']").click()
    driver.find_element(By.XPATH,"//table[@class='table table-condensed table-hover filterable-table']//thead//tr//th//input[@aria-label='option 1']").click()
    delete=driver.find_element(By.XPATH,"//button[normalize-space()='Delete Event(s)']").click()
    time.sleep(5)
    delete=driver.switch_to.alert
    print(delete.text)
    delete.accept()


# call all functions
# Login(driver)

# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)
# ValidateLogin()
# AddGroup()
cookies(driver)
time.sleep(3)
# DeleteFunctionality()
# UpdateFunctionality("save")
# createRecording()
deleteevents()

driver.quit()
