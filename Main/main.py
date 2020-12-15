from PageObjects.DrawObjects import DrawPageObjects
from Commons.CommonFunctions import Commons


def automation():
    commons = Commons()
    driver = commons.getWebDriver()
    draw = DrawPageObjects(driver)
    driver.get("http://www.htmlcanvasstudio.com/")
    draw.click_line()
    draw.draw_line()


if __name__ == '__main__':
    automation()

