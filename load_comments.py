from selenium.webdriver import ActionChains
from check_element_by_xpath import check_element_by_xpath


def load_comments(browser,url):
    browser.get(url)
    while (True):
        load_btn = check_element_by_xpath(browser,'//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li/div/button/span')
        browser.implicitly_wait(5)
        if load_btn:
            ActionChains(browser).move_to_element(load_btn).click().perform()
        else:
            print("load comment finish!")
            break
