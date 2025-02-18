from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

class JavaScriptExecution():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()

        # driver.get('https://www.letskodeit.com/practice')
        driver.execute_script("window.location = 'https://www.letskodeit.com/practice';")
        driver.implicitly_wait(3)
        time.sleep(6)
        
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")


ff = JavaScriptExecution()
ff.test()
