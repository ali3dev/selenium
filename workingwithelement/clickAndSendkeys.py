from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def test(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        login_link = driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a')
        login_link.click()

        emailField = driver.find_element(By.ID, 'email')
        emailField.send_keys('test')
        
        PasswordFiled = driver.find_element(By.ID, 'login-password')
        PasswordFiled.send_keys('test')

        time.sleep(3)
        emailField.clear()
        time.sleep(3)

        emailField.send_keys('test')
        


ff = ClickAndSendKeys()
ff.test()



