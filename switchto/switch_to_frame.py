from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")
        driver.switch_to.frame("courses-iframe")

        time.sleep(2)
        searchBox = driver.find_element(By.ID, 'search')
        searchBox.send_keys("Python")
        time.sleep(2)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, 'name').send_keys("Test Successful")



ff = SwitchToFrame()
ff.test()

