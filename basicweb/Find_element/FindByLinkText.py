from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByLink():
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementByLinkText = driver.find_element(By.LINK_TEXT, 'HOME')
        if elementByLinkText is not None:
            print('Element Found -> By Link Text')

        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, 'COURSES')
        if elementByPartialLinkText is not None:
            print('Element Found -> By Partial Link')

FindByLink = FindByLink()
FindByLink.test()
