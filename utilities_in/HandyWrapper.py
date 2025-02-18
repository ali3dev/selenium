from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        locators = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "classname": By.CLASS_NAME,
            "linktext": By.LINK_TEXT
        }
        return locators.get(locatorType, None)  # Return None if not found

    def getElement(self, locator, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            if byType is None:
                print(f"Locator type {locatorType} is not correct or supported.")
                return None
            element = self.driver.find_element(byType, locator)
            print("Element Found")
            return element
        except NoSuchElementException:
            print("Element not found")
            return None

    def isElementPresent(self, locator, locatorType="id"):
        byType = self.getByType(locatorType)
        if byType is None:
            print(f"Locator type {locatorType} is not correct or supported.")
            return False
        try:
            self.driver.find_element(byType, locator)
            print("Element Found")
            return True
        except NoSuchElementException:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, locatorType="id"):
        byType = self.getByType(locatorType)
        if byType is None:
            print(f"Locator type {locatorType} is not correct or supported.")
            return False
        try:
            elementList = self.driver.find_elements(byType, locator)
            if elementList:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except NoSuchElementException:
            print("Element not found")
            return False
