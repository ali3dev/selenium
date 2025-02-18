from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://www.letskodeit.com/home"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        # Login -> Click on "SIGN IN"
        driver.find_element(By.LINK_TEXT, "SIGN IN").click()

        email = driver.find_element(By.ID, "email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "login-password")
        password.send_keys("abcabc")

        driver.find_element(By.ID, "login").click()

        # Search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")

        # Select Course using dynamic XPath
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()


ff = DynamicXPathFormat()
ff.test()
