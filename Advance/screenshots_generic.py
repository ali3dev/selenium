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



    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "D:\\Selenium\\Advance\\test.png"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshots()
ff.test()