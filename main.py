import os
import urllib3
import urllib.request
import requests
from http.client import HTTPConnection
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# url = "https://www.instagram.com/p/Bs-_Cqvnm6Z/"
# cont = requests.get(url)
# soup = BeautifulSoup(cont.content, 'html.parser')

# image_src = soup.find("meta", property="og:image")
# print(image_src["content"] if image_src else "Cant find original image")


#TODO need a web driver or selenium or something

sam_url = 'https://www.instagram.com/samwluby/'
main_class = 'FyNDV'
row_class = 'Nnq7C weEfm'
pic_class = 'v1Nh3 kIKUG  _bz0w'

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(sam_url)
browser.find_element_by_tag_name("body").send_keys(Keys.END)


# have to use xpath since 'find_elements_by_class' doesnt allow for classes with spaces in name
rows = browser.find_elements_by_xpath("//*[contains(@class,'{0}')]".format(row_class))
for row in rows:
    row = row.text
    print("ROW: {0}" .format(row))

pics = browser.find_elements_by_xpath("//*[contains(@class,'{0}')]".format(pic_class))
for pic in pics:
    href = pic.find_element_by_css_selector('a').get_attribute('href')
    print(href)
    