from pages.droppable import Droppable
from selenium.webdriver import  ActionChains
from  conftest import browser

import time

def test_drag_and_drop(browser):
    drag_and_drop_page = Droppable(browser)
    action_chains = ActionChains(browser)
    drag_and_drop_page.visit()
    action_chains.drag_and_drop(
        drag_and_drop_page.drag.find_element(), #
        drag_and_drop_page.drob.find_element() #tager
    ).perform()
    time.sleep(2)
    assert drag_and_drop_page.drob.check_css('background-color', 'rgba(70, 130, 180, 1)')

    action_chains.drag_and_drop_by_offset(drag_and_drop_page.drag.find_element(),-200, 0).perform()
    time.sleep(2)
    assert drag_and_drop_page.drob.check_css('background-color','rgba(70, 130, 180, 1)' )

