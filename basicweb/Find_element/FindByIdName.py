from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByidName():
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, 'displayed-text')
        if element is not None:
            print('Element Found -> By ID')

        elementByName = driver.find_element(By.NAME, 'show-hide')
        if elementByName is not None:
            print('Element Found -> By Name')

findByIdName = FindByidName()
findByIdName.test()
