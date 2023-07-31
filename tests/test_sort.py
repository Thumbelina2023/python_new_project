from pages.webtables import WebTables
import time

def test_sort(browser):
    webtables_page = WebTables(browser)
    webtables_page.visit()
    webtables_page.colum_firstname.click()
    assert 'rt-th rt-resizable-header -sort-asc -cursor-pointer' in webtables_page.colum_firstname.get_dom_attribute('class')
    webtables_page.colum_firstname.click()
    assert 'rt-th rt-resizable-header -sort-desc -cursor-pointer' in webtables_page.colum_firstname.get_dom_attribute('class')

    webtables_page.colum_lastname.click()
    assert 'rt-th rt-resizable-header -sort-asc -cursor-pointer' in webtables_page.colum_lastname.get_dom_attribute('class')
    webtables_page.colum_lastname.click()
    assert 'rt-th rt-resizable-header -sort-desc -cursor-pointer' in webtables_page.colum_lastname.get_dom_attribute('class')

    webtables_page.colum_age.click()
    assert 'rt-th rt-resizable-header -sort-asc -cursor-pointer' in webtables_page.colum_age.get_dom_attribute('class')
    webtables_page.colum_age.click()
    assert 'rt-th rt-resizable-header -sort-desc -cursor-pointer' in webtables_page.colum_age.get_dom_attribute('class')

    webtables_page.colum_email.click()
    assert 'rt-th rt-resizable-header -sort-asc -cursor-pointer' in webtables_page.colum_email.get_dom_attribute('class')
    webtables_page.colum_email.click()
    assert 'rt-th rt-resizable-header -sort-desc -cursor-pointer' in webtables_page.colum_email.get_dom_attribute('class')

    webtables_page.colum_salary.click()
    assert 'rt-th rt-resizable-header -sort-asc -cursor-pointer' in webtables_page.colum_salary.get_dom_attribute('class')
    webtables_page.colum_salary.click()
    assert 'rt-th rt-resizable-header -sort-desc -cursor-pointer' in webtables_page.colum_salary.get_dom_attribute('class')

    webtables_page.colum_department.click()
    assert 'rt-th rt-resizable-header -sort-asc -cursor-pointer' in webtables_page.colum_department.get_dom_attribute('class')
    webtables_page.colum_department.click()
    assert 'rt-th rt-resizable-header -sort-desc -cursor-pointer' in webtables_page.colum_department.get_dom_attribute('class')













    time.sleep(2)

    #assert