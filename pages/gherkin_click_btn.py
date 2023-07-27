from pages.base_page import  BasePage
from components.components import WebElement

class Gherkin_click_btn(BasePage):
    def __init__(self, driver):

        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements/'
        self.btn_click = WebElement(driver,'#content > div > button')
        self.btn_delete = WebElement(driver, '#elements>button')
        super().__init__(driver, self.base_url)
