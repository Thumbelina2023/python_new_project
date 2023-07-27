from pages.webtables import WebTables
import time

def test_web_tables(browser):
    webtables = WebTables(browser)
    webtables.visit()

    assert webtables.btn_add.exist()
    webtables.btn_add.click()
    assert webtables.modal_content.exist()

    # сабмит пустой

    webtables.first_name.send_keys('Olga')
    webtables.last_name.send_keys('Ivanova')
    webtables.email.send_keys('olga@mail.ru')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('10000')
    webtables.department.send_keys('Logistic')
    webtables.submit.click()
    assert not webtables.modal_content.visible()
    for first_n in webtables.first_name_table.find_element:
        assert first_n.text == 'Olga'
    #for last_n in webtables.lat_name_table.find_element:
       # assert last_n.text == 'Ivanova'
    time.sleep(2)