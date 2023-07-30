from pages.base_page import  BasePage
from components.components import WebElement

class Inputs(BasePage):
    def __init__(self, driver):

        self.base_url = 'https://the-internet.herokuapp.com/inputs'
        self.field = WebElement(driver,'#content > div > div > div > input[type=number]')
        super().__init__(driver, self.base_url)
