from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.alert import Alert
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
import pytest
import time
@pytest.mark.parametrize("pages", [Accordion, Alert, DemoQa, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.head_meta.exist()
    assert  page.head_meta.get_dom_attribute('name') == 'viewport'
    assert page.head_meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'