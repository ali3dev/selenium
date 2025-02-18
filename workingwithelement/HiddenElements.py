from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HiddenElements():
    def testLetsKodeIt(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        textBoxElement = driver.find_element(By.ID, 'displayed-text')
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

         # Click the Hide button
        driver.find_element(By.ID, "hide-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        driver.execute_script("window.scrollBy(0, -150);")
        # Click the Show button
        driver.find_element(By.ID, "show-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)
        # Browser Close
        driver.quit()

    def testExpedia(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.ID, 'tab-flight-tab').click()
        drpdwnElement = driver.find_element_by_id("flight-age-select-1")
        print("Element visible? " + str(drpdwnElement.is_displayed()))
 
ff = HiddenElements()
ff.testLetsKodeIt()
ff.testExpedia()