from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RunChromeTests():

    def test(self):
        # Provide the path to geckodriver executable
        chromedriver_path = 'D:\\Selenium\\driver\\chromedriver.exe'

        # Initialize the Service object with geckodriver path
        service = Service(executable_path=chromedriver_path)

        # Initialize the Firefox driver with the service
        driver = webdriver.Chrome(service=service)

        # Open the desired URL
        driver.get('https://www.letskodeit.com')


chrome_Run = RunChromeTests()
chrome_Run.test()