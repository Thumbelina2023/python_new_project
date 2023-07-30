from pages.webtables import WebTables
import time

def test_web_tables(browser):
    webtables = WebTables(browser)
    webtables.visit()
    webtables.rows.click()
    time.sleep(2)
    webtables.btn_next.click()
    assert webtables.btn_next.get_dom_attribute('disabled') #== 'Next'
    webtables.btn_prev.click()
    assert webtables.btn_prev.get_dom_attribute('disabled') #== 'Previous'

    for i in range(3):
        webtables.btn_add.click()
        webtables.first_name.send_keys('Olga')
        webtables.last_name.send_keys('Ivanova')
        webtables.email.send_keys('olga@mail.ru')
        webtables.age.send_keys('30')
        webtables.salary.send_keys('10000')
        webtables.department.send_keys('Logistic')
        webtables.submit.click()

    time.sleep(2)
    assert webtables.page_of.get_text() == '2'
    assert not webtables.btn_next.get_dom_attribute('disabled')

    webtables.btn_next.click()
    assert webtables.page.get_dom_attribute('value') == '2'

    webtables.btn_prev.click()
    assert webtables.page.get_dom_attribute('value') == '1'



