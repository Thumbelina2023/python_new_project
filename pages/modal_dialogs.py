from pages.base_page import  BasePage
from components.components import WebElement

class modal_dialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_modal_dialog = WebElement(driver,'#item-0')
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_smollmodal = WebElement(driver,'#showSmallModal')
        self.btn_largemodal = WebElement(driver,'#showLargeModal')
        self.btn_smollmodal_close = WebElement(driver,'#closeSmallModal')
        self.btn_largemodal_close = WebElement(driver,'#closeLargeModal')
        self.modal_window_smoll = WebElement(driver,'body > div.fade.modal.show > div > div')
        self.modal_window_large = WebElement(driver,'body > div.fade.modal.show > div > div')
