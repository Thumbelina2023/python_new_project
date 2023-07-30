from selenium.webdriver.common.by import By

from pages.base_page import  BasePage
from components.components import WebElement


class DemoQa(BasePage): # метод, котрый принимает find_element с аргументом locator

    def __init__(self, driver):
        self.icon = WebElement(driver, '#app > header > a') # связываем наш ... с новым webelemet классом в компонентах
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div >div:nth-child(1)')
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.h5 = WebElement(driver, 'div > div.card-body > h5')







