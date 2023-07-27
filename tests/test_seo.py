from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.alert import Alert
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
import pytest
import time


def test_seo(browser):
    seo = DemoQa(browser)

    seo.visit()
    assert browser.title == 'DEMOQA'

@pytest.mark.parametrize("pages", [Accordion, Alert, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'