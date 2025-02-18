from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time 

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.plupload.com/examples/")
driver.find_element(By.ID, "uploader_browse").click()
time.sleep(3)

Keyboard = Controller()


Keyboard.type("C:\\Users\\HP\\OneDrive\\Desktop\\recoment.jpg")
Keyboard.press(Key.enter)
Keyboard.release(Key.enter)


# C:\Users\HP\OneDrive\Pictures\ali.jpg