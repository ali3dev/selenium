from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByXPathCSS():
    def test(self):
        url = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)

        elementXPath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementXPath is not None:
            print("Element Found -> By XPATH")
        elementByCSS = driver.find_element(By.CSS_SELECTOR, '#displayed-class')
        if elementByCSS is not None:
            print("Element Found -> By CSS")

run_test = FindByXPathCSS()
run_test.test()
