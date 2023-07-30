from pages.alert import Alert
import time

def test_check_alert(browser):
    check_alert = Alert(browser)
    check_alert.visit()

    check_alert.btn_timer.click()
    time_temp = 0
    while True: #бесконечный цикл
        time.sleep(1)
        time_temp +=1
        if time_temp == 5:
            assert check_alert.alert()
            check_alert.alert().accept()
            break
        else:
            assert not check_alert.alert()
    time.sleep(6)




