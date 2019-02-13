import os
import requests
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request


sam_url = 'https://www.instagram.com/samwluby/'
main_class = 'FyNDV'
row_class = 'Nnq7C weEfm'
pic_class = 'v1Nh3 kIKUG  _bz0w'


def load_full_browser_page(url):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    return browser

def get_pic_urls(browser):
    pic_urls = []

    # have to use xpath since 'find_elements_by_class' doesnt allow for classes with spaces in name
    rows = browser.find_elements_by_xpath("//*[contains(@class,'{0}')]".format(row_class))
    for row in rows:
        row = row.text

    pics = browser.find_elements_by_xpath("//*[contains(@class,'{0}')]".format(pic_class))
    for pic in pics:
        href = pic.find_element_by_css_selector('a').get_attribute('href')
        print(href)
        pic_urls.append(href)

    return pic_urls

def get_pic_page_source(pic_url):
    source = requests.get(pic_url)
    source = BeautifulSoup(source.content, 'html.parser')
    try:
        orig = source.find("meta", property="og:image")
        print(orig["content"])
        return orig["content"]
    except:
        print("Cant find original image")

def save_images(url_list):
    for index, url  in enumerate(url_list):
        urllib.request.urlretrieve(url, "insta_{0}.jpg".format(index))

def main():
    try:
        profile = sys.argv[1]
        insta_url = 'https://www.instagram.com/{0}/'.format(profile)
        browser = load_full_browser_page(insta_url)
        pic_urls = get_pic_urls(browser)
        orig_pic_urls = []
        for pic in pic_urls:
            orig_pic_urls.append(get_pic_page_source(pic))
        save_images(orig_pic_urls)

    except:
        print("Enter a profile name")
   

if __name__ == '__main__':
    main()
      