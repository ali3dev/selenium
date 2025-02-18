from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():
    def testListOfElements(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        # size = len(radioButtonsList)
        # print("Size of RadioButttonList is :" + str(radioButtonsList))

        for radioButtons in radioButtonsList:
            isSelected = radioButtons.is_selected()
            if not isSelected:
                radioButtons.click()
                time.sleep(2)

ff = WorkingWithElementsList()
ff.testListOfElements()


    
