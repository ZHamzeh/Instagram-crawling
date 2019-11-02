def login(browser,username,password):
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    browser.implicitly_wait(1)
    browser.maximize_window()
    UserName_box = browser.find_element_by_name('username')
    browser.implicitly_wait(1)
    UserName_box.send_keys(username)
    browser.implicitly_wait(1)

    Pass_box = browser.find_element_by_name('password')
    browser.implicitly_wait(1)
    Pass_box.send_keys(password)
    browser.implicitly_wait(1)

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
    browser.implicitly_wait(1)
