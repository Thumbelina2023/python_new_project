from pages.webtables import WebTables
import time

def test_web_tables(browser):
    webtables = WebTables(browser)
    webtables.visit()
    assert not webtables.no_row_found.exist()
    while webtables.delete.exist():
        webtables.delete.click()

    assert webtables.no_row_found.exist()