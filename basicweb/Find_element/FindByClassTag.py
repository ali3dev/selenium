from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FindByClassTag():
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementByClassName = driver.find_element(By.CLASS_NAME, 'inputs')
        if elementByClassName is not None:
            print('Element Found -> By Class Nsme')
            elementByClassName.send_keys('Testing')

        elementByTagName = driver.find_element(By.TAG_NAME, 'a')
        if elementByTagName is not None:
            print('Element Found -> By Tag Name')
        
        time.sleep(10)

findByTag = FindByClassTag()
findByTag.test()
