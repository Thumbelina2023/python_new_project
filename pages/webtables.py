from pages.base_page import  BasePage
from components.components import WebElement
import time

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables/'

        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_content = WebElement(driver,'body > div.fade.modal.show > div > div')
        self.first_name = WebElement(driver,'#firstName')
        self.last_name = WebElement(driver,'#lastName')
        self.email = WebElement(driver,'#userEmail')
        self.age = WebElement(driver,'#age')
        self.salary = WebElement(driver,'#salary')
        self.department = WebElement(driver,'#department')
        self.submit = WebElement(driver,'#submit')
        self.first_name_table = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth')
       # self.lat_name_table = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth')
        self.email_table = WebElement(driver,'')
        self.form = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table')
        self.no_row_found = WebElement(driver,'div.rt-noData')
        self.delete = WebElement(driver, '[title="Delete"]')

