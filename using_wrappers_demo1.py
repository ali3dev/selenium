from selenium import webdriver
from utilities_in.HandyWrapper import HandyWrappers
import time

class UsingWrappers1():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

ff = UsingWrappers1()
ff.test()