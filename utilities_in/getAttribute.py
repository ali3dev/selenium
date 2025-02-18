from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetAttribute():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        element = driver.find_element(By.ID, "name")
        result = element.get_attribute("class")

        print("Value of attribute is: " + result)
        time.sleep(1)
        driver.quit()


ff = GetAttribute()
ff.test()