from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "http://www.goibibo.com"
driver = webdriver.Firefox  ()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(3)
partialText = "Del"
textToSelect = "Delhi, India(DEL)"

popup = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/span/span')
popup.click()

textElement = driver.find_element(By.ID, "")
textElement.send_keys(partialText)

ulElement = driver.find_element(By.ID, "autoSuggest-list")
inner_html = ulElement.get_attribute("innerHTML")
# print(inner_html)

liElements = ulElement.find_elements(By.TAG_NAME, "li")
time.sleep(2)

for element in liElements:
    if textToSelect in element.text:
        element.click()
        break

time.sleep(4)

driver.quit()