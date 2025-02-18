from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ElementState:
    def test(self):
        baseurl = "http://www.google.com"
        
        # Initialize WebDriver for Firefox
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        try:
            # Locate the Google search bar
            search_box = driver.find_element(By.NAME, "q")  # Google's search bar uses the "name" attribute 'q'
            
            # Check if the element is enabled
            if search_box.is_enabled():
                print("Search box is enabled.")
                
                # Enter the search query
                search_query = "Ali Arslan Khan"
                search_box.send_keys(search_query)

                # Submit the search query
                search_box.send_keys(Keys.ENTER)

                # Wait for the results to load
                time.sleep(3)

                # Click on the first search result
                first_result = driver.find_element(By.XPATH, "(//h3)[1]")  # XPath for the first search result's title
                first_result.click()

                print(f"Clicked on the first search result for '{search_query}'")
            else:
                print("Search box is not enabled.")
        except Exception as ex:
            print("Error occurred:", ex)
        finally:
            # Close the browser
            driver.quit()

# Instantiate and call the method correctly
e = ElementState()
e.test()
