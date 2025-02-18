from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class DropdownSelect():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, 'carselect')
        sel = Select(element)

        sel.select_by_value('benz')
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by value")
        time.sleep(2)

        sel.select_by_visible_text('BMW')
        print("Select BMW by value")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")

ff = DropdownSelect()
ff.test()

