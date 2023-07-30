from pages.gherkin_inputs import Inputs
from selenium.webdriver.common.keys import Keys
import time

def test_input(browser):
    input_page = Inputs(browser)
    input_page.visit()
    assert input_page.field.exist()


    for i in ['1','-','e','-1','1e','-e', '-1e']:
        input_page.field.send_keys(i)
        assert input_page.field.get_text() == ''
        input_page.field.clear()

    for i in ['a','+','@','%','1a','-d',]:

       input_page.field.send_keys(i)
       assert not i in input_page.field.get_text()
       input_page.field.clear()

    input_page.field.send_keys('1')
    for a in range(4):
        input_page.field.send_keys(Keys.UP)

    for b in range(6):
        input_page.field.send_keys(Keys.DOWN)

    time.sleep(2)