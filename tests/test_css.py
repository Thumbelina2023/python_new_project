from pages.elements_page import ElementsPage

def test_flex_menu(browser):
    elem = ElementsPage(browser)
    elem.visit()
    assert elem.elem_row.check_css('flex', '0 0 25%')
    assert elem.elem_row.check_css('max-width','25%')
    browser.set_window_size(659, 1000)

    assert elem.elem_row.check_css('flex', '0 0 100%')
    assert elem.elem_row.check_css('max-width', '100%')
    browser.set_window_size(1000, 1000)