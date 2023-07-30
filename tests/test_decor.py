from pages.demoqa import DemoQa
from pages.radio_button import RadioButton
import pytest
import time

def test_decor(browser):
    dec = DemoQa(browser)
    dec.visit()
    assert dec.h5.check_count_elements(count=6)
    for elem in dec.h5.find_elements():
            assert elem.text != ''
@pytest.mark.skip
def test_decor_3(browser):
    demo = DemoQa(browser)


#@pytest.mark.skipif(True,reason='просто пропуск')

def test_decor_radio_btn(browser):
    dec_rad_btn = RadioButton(browser)

    if not dec_rad_btn.code_status():
        pytest.skip(reason=f'Страница {dec_rad_btn.base_url} недоступна')
    dec_rad_btn.visit()
    dec_rad_btn.btn_yes.click_force()
    assert dec_rad_btn.yes_text.get_text() == 'You have selected Yes'
    dec_rad_btn.btn_impressive.click_force()
    assert dec_rad_btn.impressive_text.get_text() == 'You have selected Impressive'
    #assert dec_rad_btn.btn_no.get_dom_attribute('class') == 'disabled'
    assert 'disabled' in dec_rad_btn.btn_no.get_dom_attribute('class')