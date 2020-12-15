from selenium.webdriver import ActionChains


class DrawPageObjects:
    def __init__(self,driver):
        self.driver=driver
        self.line_xpath = "//input[@title='Draw a line']"
        self.canvas_xpath="//canvas[@id='imageTemp']"

    def click_line(self):
        self.driver.find_element_by_xpath(self.line_xpath).click()

    def draw_line(self):
        driver=self.driver
        action = ActionChains(driver)
        canvasElement = driver.find_element_by_xpath(self.canvas_xpath)
        action.move_to_element_with_offset(canvasElement, 135, 90).click().move_by_offset(0,90).double_click().perform()
        action.move_to_element_with_offset(canvasElement, 90, 135).click().move_by_offset(90,0).double_click().perform()