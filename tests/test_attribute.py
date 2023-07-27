from pages.text_box import TextBox

def test_placeholder(browser):
    placeceholder = TextBox(browser)
    placeceholder.visit()
    assert  placeceholder.full_name.get_dom_attribute('placeholder') == 'Full Name'
