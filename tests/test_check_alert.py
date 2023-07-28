from pages.alert import Alert
import time

def test_check_alert(browser):
    check_alert = Alert(browser)
    check_alert.visit()

    check_alert.btn_timer.click()
    time.sleep(6)
    assert check_alert.alert()
    check_alert.alert().accept()



