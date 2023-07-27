from pages.alert import Alert
import time

def test_allert(browser):
    allert = Alert(browser)
    allert.visit()
    assert allert.alert()
    #assert not allert.alert()
    allert.btn_alert.click()

    assert allert.alert()
    allert.alert().accept() #метот аccепт не дает тесту упасть

    allert.btn_alert.click()
    assert allert.alert().text == 'You clicked a button'
    allert.alert().accept()
    #assert not allert.alert()

def test_confirm(browser):
    alert_confirm = Alert(browser)
    alert_confirm.visit()
    alert_confirm.btn_confirm.click()
    time.sleep(2)
    alert_confirm.alert().dismiss()
    assert alert_confirm.confirmResult.get_text() == 'You selected Cancel'

def test_promt(browser):
    prom = Alert(browser)
    prom.visit()
    prom.btn_promt.click()
    time.sleep(2)
    name = 'olga'
    prom.alert().send_keys(name)
    prom.alert().accept()
    assert prom.promResult.get_text() == f'You entered {name}'
