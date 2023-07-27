from pages.browser_tab import BrowserTab
import time

def test_browser_tab(browser):
    browser_tab_page = BrowserTab(browser)
    browser_tab_page.visit()

    #метод возвращает список всех открытыхвкладок browser.window_handles

    assert len(browser.window_handles) == 1
    browser_tab_page.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2 # проверяем, что вкладок уже 2 стало

  # метод переключени вкладок

    browser.switch_to.window(browser.window_handles[0])


