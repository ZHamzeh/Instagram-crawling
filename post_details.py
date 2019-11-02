from xlwt import Workbook
from selenium import webdriver
from check_element_by_xpath import check_element_by_xpath

def post_details(browser,post_number,url,comment_number):
    print("00")
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    browser.get(url)

    userid_element = check_element_by_xpath(browser,'//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[1]/h2/a')
    if userid_element:
        username = userid_element.text
    else:
        username = ''


    #user_date = browser.find_element_by_xpath('// *[ @ id = "react-root"] / section / main / div / div / article / div[2] / div[2] / a / time')
    user_date = check_element_by_xpath(browser,'//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/div/div/time')
    if user_date:
        date = user_date.get_attribute('title')
    else:
        date= ''

    post_like =  check_element_by_xpath(browser,'//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button')
    if post_like :
        post_like = post_like.text
    else:
        post_like = ''


    post_caption = check_element_by_xpath(browser,'//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span')
    if post_caption:
        post_caption = post_caption.text
    else:
        post_caption = ''


    sheet1.write(0, 0, username)
    sheet1.write(0, 1, date)
    sheet1.write(0, 2, post_like)
    sheet1.write(0, 3, comment_number)
    sheet1.write(0, 4, post_caption)

    counter = 1
    k=0
    print("55")
    #while (counter<comment_number):
    while(k<2):
        k+=1
        print("countter= ",counter)

        #comment_username = browser.find_elements_by_xpath(
        #    '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[%s]/div/li/div/div/div[2]/h3/a' % counter)
        comment_username = browser.find_elements_by_xpath(
            '// *[ @ id = "react-root"] / section / main / div / div / article / div[2] / div[1] / ul/ul[%s]'%counter)
        print("ccc",len(comment_username))
        for u in range(len(comment_username)):
            print ("uuu",comment_username[u].text)
        #comment_username = comment_username.text
        #print (comment_username,": username")
        browser.implicitly_wait(10)

        # comment_date = browser.find_element_by_xpath(
        #      '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[%s]/div/li/div/div/div[2]/div/div/time' % counter)
        # print(comment_date)
        # comment_date = comment_date.text
        # print(comment_date," date")
        # browser.implicitly_wait(10)
        #
        # comment_text = browser.find_element_by_xpath(
        #     '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[%s]/div/li/div/div/div[2]/span' % counter)
        # comment_text = comment_text.text
        # print(comment_text)
        # browser.implicitly_wait(10)
        #
        # comment_like = browser.find_element_by_xpath(
        #     '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[%s]/div/li/div/div/div[2]/div/div/button[1]' % counter)
        # comment_like = comment_like.text
        # if (comment_like=='Reply'):
        #     comment_like = '0 like'
        # print(comment_like,"like")
        # browser.implicitly_wait(10)
        #
        #
        # sheet1.write(counter, 0, comment_username )
        # sheet1.write(counter, 1, comment_date)
        # sheet1.write(counter, 2, comment_like)
        # sheet1.write(counter, 3, comment_text)

        counter +=1

    excel_name='%s_%s.xls'%(username,post_number)
    wb.save(excel_name)
    print("ok")

browser = webdriver.Chrome('chromedriver.exe')
post_details(browser,1,'https://www.instagram.com/p/Boi0JoIFxu8/?utm_source=ig_web_copy_link',5)

