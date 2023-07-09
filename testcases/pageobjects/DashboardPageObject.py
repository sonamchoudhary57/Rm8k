from selenium import webdriver
from selenium.webdriver.common.by import By

class DashboardPage:

    #Locators
    #add grp
     btn_addgrp_xpath="//i[@title='Add Group']"
     txtbox_grpname_id="formGridAddress1"
     btn_selectgrp_xpath="//button[normalize-space()='Select Parent Group']"
     txt_selectgrp_xpath="//a[normalize-space()='root']"
     btn_savegrp_xpath="//button[normalize-space()='Submit']"


     #add device
     btn_adddevice_xpath="//i[@title='Add Device']"
     txtbox_sourceurl_id="sourceAddress"
     btn_selgrp_xpath="//button[normalize-space()='Select Group']"
     txt_selgrp_xpath="//a[normalize-space()='root']"
     btn_savedevice_xpath="//button[normalize-space()='Save']"

     #update device
     btn_update_xpath="//i[@title='Update Checked Device']"
     btn_configure_xpath="//button[normalize-space()='Configure RemoteControls']"

     #for remote popup
     btn_savecofg_xpath="//button[@class='btn-fill btn btn-dark']"
     btn_cancelcofg_xpath="//button[@class='btn-fill btn btn-primary']"

     #for update popup
     btn_savecofg_xpath="//button[normalize-space()='Save']"
     btn_cancelcofg_xpath="//button[normalize-space()='Cancel']"




     # delete locators
     btn_delete_xpath="//button[@title='Delete Checked Devices/Groups']"


     # single player 
     tn_delete_xpath="//button[@title='Single Player']"



      #constructor
     def __init__(self,driver):
        self.driver=driver

    
     #action methods
     def addGrp(self,grpname):
         self.driver.find_element(By.ID,self.txtbox_grpname_id).send_keys(grpname)
         self.driver.find_element(By.XPATH,self.btn_selectgrp_xpath).click()
         self.driver.find_element(By.XPATH,self.txt_selectgrp_xpath).click()
         self.driver.find_element(By.XPATH,self. btn_savegrp_xpath).click()
         
         
         