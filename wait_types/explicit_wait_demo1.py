from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo1():
    def test(self):
        baseUrl = "https://www.letskodeit.com/courses"
        driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.get(baseUrl)
        driver.execute_script("window.location = 'https://www.letskodeit.com/courses';")
        # driver.find_element(By.XPATH, "//a[text()='Sign In']").click()

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                                                ignored_exceptions=[NoSuchElementException,
                                                                    ElementNotVisibleException,
                                                                    ElementNotSelectableException])
        
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a')))
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo1()
ff.test()