from pages.base_page import  BasePage
from components.components import WebElement

class Gherkin_btn_add(BasePage):
    def __init__(self, driver):

        self.base_url = 'https://the-internet.herokuapp.com/'
        self.add_remove_elem = WebElement(driver,'#content > ul > li:nth-child(2) > a')
        super().__init__(driver, self.base_url)
