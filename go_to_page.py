def go_to_page(browser,url_page):
    browser.implicitly_wait(10)
    browser.get(url_page)
    browser.implicitly_wait(10)
