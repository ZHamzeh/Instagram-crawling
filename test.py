from selenium import webdriver
from login import login
from go_to_page import go_to_page
from post_of_page import post_of_page
from load_comments import load_comments
from file import read_file
from post_details import post_details

browser = webdriver.Chrome('chromedriver.exe')
file = 'main.txt'

username = 'tarbiate_jensi1'
password = 'miri13676949'

url_page = 'https://www.instagram.com/tarbiate_jensi1/'

#login(browser,username,password)
go_to_page(browser,url_page)
print("go_to_page")

if post_of_page(browser,file):
    list_of_post = read_file('main.txt')
    lenght_of_list = int(len(list_of_post)/3)

    for i in range(lenght_of_list):
        print("i= ",i)
        counter = 3*i
        load_comments(browser,list_of_post[counter+1])

        post_details(browser,list_of_post[counter],list_of_post[counter+1],list_of_post[counter+2])

    print("done")

else:
    print("post of page is not find!")
