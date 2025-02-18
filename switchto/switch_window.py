from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SwitchToWindow():
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        driver.find_element(By.ID, 'openwindow').click()
        time.sleep(2)

        handles = driver.window_handles

        for handle in handles:
            if handle != parentHandle:
                driver.switch_to.window(handle)
                print("Switched to: " + handle)
                break

        try:
            # Wait for element
            searchBox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "search"))
            )

            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView();", searchBox)

            # Click to focus
            searchBox.click()

            # Send keys
            searchBox.send_keys('python')
            print("Search executed successfully!")

        except Exception as e:
            print("Error:", e)

        # Close new window and switch back
        driver.close()
        driver.switch_to.window(parentHandle)
        print("Switched back to parent window.")

ff = SwitchToWindow()
ff.test()
