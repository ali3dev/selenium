from selenium import webdriver
from selenium.webdriver.edge.service import Service


class RunEdgeTests():

    def test(self):
        # Provide the path to geckodriver executable
        edgedriver_path = 'D:\\Selenium\\driver\\msedgedriver.exe'

        # Initialize the Service object with geckodriver path
        edgeservice = Service(executable_path=edgedriver_path)

        # Initialize the Firefox driver with the service
        driver = webdriver.Edge(service=edgeservice)

        # Open the desired URL
        driver.get('https://www.letskodeit.com')


edge_Run = RunEdgeTests()
edge_Run.test()