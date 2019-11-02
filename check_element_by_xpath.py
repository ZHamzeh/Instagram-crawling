from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

def check_element_by_xpath(browser,xpath):
    counter =0
    while (counter<5):
        browser.implicitly_wait(3)
        try:
            element = browser.find_element_by_xpath(xpath)
            browser.implicitly_wait(3)
            return element
        except NoSuchElementException as e:
            counter += 1

        except ElementNotVisibleException as e:
            counter += 1

        except TimeoutException as e:
            counter += 1

        except Exception as e:
            counter += 1

    return False
