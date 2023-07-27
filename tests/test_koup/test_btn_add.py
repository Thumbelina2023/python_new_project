from pages.gherkin_btn_add import Gherkin_btn_add
from pages.gherkin_click_btn import Gherkin_click_btn
import time


def test_open_page(browser):
    btn_add = Gherkin_btn_add(browser)
    add_remove = Gherkin_click_btn(browser)
    btn_add.visit()

    assert btn_add.add_remove_elem.get_text() == 'Add/Remove Elements'
    btn_add.add_remove_elem.click()
    time.sleep(2)
    assert add_remove.equal_url()
    assert add_remove.btn_click.get_text() == 'Add Element'
    assert add_remove.btn_click.get_dom_attribute('onclick') == 'addElement()'
    for i in range(4):

        add_remove.btn_click.click()

    assert add_remove.btn_delete.check_count_elements(count=4)

    for element in add_remove.btn_delete.find_elements():
        assert element.text == 'Delete'

    for i in range(4):
        add_remove.btn_delete.click()

    assert not add_remove.btn_delete.exist()
    time.sleep(3)



