from selenium import webdriver


class Commons:

    def __init__(self):
        pass

    def getWebDriver(self):
        driver = webdriver.Chrome('C:\Selenium\selenium-java-3.141.59\chromedriver.exe')
        driver.maximize_window()
        return driver
