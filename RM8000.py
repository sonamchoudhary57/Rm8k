from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome() 
driver.implicitly_wait(10)

driver.get("http://44.211.158.119/login")

driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME,"username").send_keys("sonam")
driver.find_element(By.NAME,"password").send_keys("radiant")
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
time.sleep(5)


act_title=driver.title
exp_title="Radiant RM8000 Series"
if act_title==exp_title:
    print("Login test passed")
else:
    print("login test failed")

#ADD GROUP

addgrp=driver.find_element(By.XPATH,"//i[@title='Add Group']")
addgrp.click()

driver.find_element(By.NAME,"name").send_keys("G6135")
driver.find_element(By.XPATH,"//button[normalize-space()='Select Parent Group']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='root']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
# elements = driver.find_elements(By.CLASS_NAME,"rct-icon rct-icon-uncheck")

# for x in elements:    
#     print(x)
#     x.click()


#grpname=mywait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'G2')]")))
# exp_grp= "G1"
# if (grpname==exp_grp):
#     print("add grp passed")
# else:
#     print("add grp failed")

time.sleep(3)



 #ADD DEVICE   
driver.find_element(By.XPATH,"//button[@title='Add Device']").click()
add_device=driver.find_element(By.ID,"sourceAddress")
add_device.send_keys("http://50.239.254.200")
driver.find_element(By.XPATH,"//button[normalize-space()='Select Group']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='root']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

time.sleep(3)




#Delete funtionality 
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
checkboxes = driver.find_elements(By.XPATH, "//span[contains(@class, 'rct-icon-uncheck')]")
checkboxes[len(checkboxes)-1].click()
time.sleep(5)

driver.find_element(By.XPATH,"//button[@title='Update Checked Device']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Configure RemoteControls']").click()
time.sleep(5)

time.sleep(5)

#cancel update device
driver.find_element(By.XPATH,"//button[@class='btn-fill btn btn-primary']").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']").click()



# dropcountry=Select(driver.find_element(By.ID,"selectedRemoteType"))

#select option from the dropdown
# dropcountry.select_by_visible_text("Comcast Red Select")
# time.sleep(5)
# driver.find_element(By.XPATH,"//button[@class='btn-fill btn btn-dark']").click()
time.sleep(5)



#Recordings

driver.find_element(By.XPATH,"//a[normalize-space()='RECORDINGS']").click()
time.sleep(5)

# create event

driver.find_element(By.XPATH,"//button[normalize-space()='Create Event']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Select Device']").click()

#select device
device=driver.find_element(By.ID,"64991ec38de4ae31c23ac3fc")
device.click()
print(device.is_selected()) 

driver.find_element(By.XPATH,"//button[normalize-space()='Select this Device for the Event']").click()
#Enter channel name
driver.find_element(By.ID,"channel").send_keys("asdf")

# Enter event title
driver.find_element(By.ID,"eventName").send_keys("asdsfdsef")

#select mode
selectmode=Select(driver.find_element(By.XPATH,"//select[@id='sourceMode']"))
selectmode.select_by_visible_text("Scheduled Recording")
time.sleep(5)



#print all the dropdown options
alloptions=selectmode.options
for opt in alloptions:
    print(opt.text)




# driver.get_screenshot_as_file("C:/Users/User1/Desktop/Test scripts/screenshots/demo22.png")
# time.sleep(5)
driver.quit()


