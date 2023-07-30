from pages.webtables import WebTables
import time

def test_sort(browser):
    webtables_page = WebTables(browser)
    webtables_page.visit()
    webtables_page.colum_firstname.click()
    assert 'Alden' in webtables_page.name1.get_text()
    webtables_page.colum_firstname.click()
    assert 'Kierra' in webtables_page.name1.get_text()

    browser.refresh()
    webtables_page.colum_lastname.click()
    assert 'Cantrell' in webtables_page.name2.get_text()
    webtables_page.colum_lastname.click()
    assert 'Vega' in webtables_page.name2.get_text()

    browser.refresh()
    webtables_page.colum_age.click()
    assert '29' in webtables_page.name3.get_text()
    webtables_page.colum_age.click()
    assert '45' in webtables_page.name3.get_text()

    browser.refresh()
    webtables_page.colum_email.click()
    assert 'alden@example.com' in webtables_page.name4.get_text()
    webtables_page.colum_email.click()
    assert 'kierra@example.com' in webtables_page.name4.get_text()











    time.sleep(2)

    #assert