from selenium import webdriver
from wait_types.explicit_wait_type import ExplicitWaitType
import time


class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator='//*[@id="navbar-inverse-collapse"]/div/div/a', locatorType="xpath")
        
        # element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()