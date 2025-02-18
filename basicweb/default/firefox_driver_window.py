from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService


class RunFFTests():

    def test(self):
        # Provide the path to geckodriver executable
        geckodriver_path = 'D:\\Selenium\\driver\\geckodriver.exe'

        # Initialize the Service object with geckodriver path
        service = FFService(executable_path=geckodriver_path)

        # Initialize the Firefox driver with the service
        driver = webdriver.Firefox(service=service)

        # Open the desired URL
        driver.get('https://www.letskodeit.com')


ff = RunFFTests()
ff.test()