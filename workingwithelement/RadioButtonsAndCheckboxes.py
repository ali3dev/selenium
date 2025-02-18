from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class RadioButtonsAndCheckboxes():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element(By.ID, 'bmwradio')
        bmwRadioBtn.click()

        time.sleep(2)
        bnzRadioBtn = driver.find_element(By.ID ,'benzradio')
        bnzRadioBtn.click()

        time.sleep(2)
        bmwCheckBox = driver.find_element(By.ID, 'bmwcheck')
        bmwCheckBox.click()

        time.sleep(2)
        bnzCheckBox = driver.find_element(By.ID, 'benzcheck')
        bnzCheckBox.click()

        print("BMW Radio button is selected? " + str(bmwRadioBtn.is_selected())) # True if selected, False is not selected
        print("Benz Radio button is selected? " + str(bnzRadioBtn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmwCheckBox.is_selected()))
        print("Benz Checkbox is selected? " + str(bnzCheckBox.is_selected()))


ff = RadioButtonsAndCheckboxes()
ff.test()