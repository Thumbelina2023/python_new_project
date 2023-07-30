from pages.modal_dialogs import modal_dialogs
import pytest
import time

def test_check_modal(browser):
    modal_dialogs_page = modal_dialogs(browser)

    if not modal_dialogs_page.code_status():
        pytest.skip(reason=f'Страница {modal_dialogs_page.base_url} недоступна')

    modal_dialogs_page.visit()
    assert modal_dialogs_page.btn_smollmodal.exist()
    assert modal_dialogs_page.btn_largemodal.exist()
    modal_dialogs_page.btn_smollmodal.click()
    time.sleep(2)
    assert modal_dialogs_page.modal_window_smoll.exist()
    modal_dialogs_page.btn_smollmodal_close.click()
    modal_dialogs_page.btn_largemodal.click()
    time.sleep(2)
    assert modal_dialogs_page.modal_window_large.exist()
    modal_dialogs_page.btn_largemodal_close.click()
