from selenium.webdriver import ActionChains
from str_to_int import str_to_int
from check_element_by_xpath import check_element_by_xpath

def post_of_page(browser,file):
    fi = open(file,'w')
    number_of_posts = check_element_by_xpath(browser,'//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a/span')
    if number_of_posts:
        number_of_posts = number_of_posts.text
        number_of_posts = str_to_int(number_of_posts)
        row = (number_of_posts // 3) + 1
        Counter = 0

        for x in range(1, row + 1):
            for y in range(1, 4):
                print("x,y= ",x, " ",y)
                if Counter == number_of_posts:
                    break

                xpath1 = '//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[%s]/div[%s]' % (x, y)
                xpath2 = '//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[%s]/div[%s]/a' % (x, y)
                xpath_number_of_comments = '//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[%s]/div[%s]/a/div[2]/ul/li[2]/span[1]' % (
                x, y)
                post = check_element_by_xpath(browser,xpath1)
                link = check_element_by_xpath(browser,xpath2)
                browser.implicitly_wait(3)
                ActionChains(browser).move_to_element(post).perform()
                browser.implicitly_wait(3)
                number_of_comments = check_element_by_xpath(browser,xpath_number_of_comments)
                if number_of_comments:
                    number_of_comments = str_to_int(number_of_comments.text)
                else:
                    number_of_comments = ''
                fi.write(str(Counter+1)+' '+str(link.get_attribute('href')) + ' ' + str(number_of_comments) + '\n')
                Counter += 1
                print(Counter)
        fi.close()
        return True

    else:
        return False
