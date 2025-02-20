from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseUrl = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        driver.find_element(By.ID, "email").send_keys("abc@email.com")
        driver.find_element(By.ID, "login-password").send_keys("abc")
        driver.find_element(By.ID, "login").click()
        destinationFileName = "D:\\Selenium\\Advance\\test.png"  #Windows

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()