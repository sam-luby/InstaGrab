import requests
import sys
import os
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# Constants
main_class = 'FyNDV'
row_class = 'Nnq7C weEfm'
pic_class = 'v1Nh3 kIKUG  _bz0w'


# opens a google chrome browser on given url, controlled by selenium,
#  and scrolls to end of page (to load all content)
def load_full_browser_page(url):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    return browser

    # finds all instagram pictures on the given page.
    #  gets the url for each individual picture
def get_pic_urls(browser):
    pic_urls = []

    # have to use xpath since 'find_elements_by_class' doesnt allow for classes with spaces in name
    rows = browser.find_elements_by_xpath(
        "//*[contains(@class,'{0}')]".format(row_class))
    for row in rows:
        row = row.text

    pics = browser.find_elements_by_xpath(
        "//*[contains(@class,'{0}')]".format(pic_class))
    for pic in pics:
        href = pic.find_element_by_css_selector('a').get_attribute('href')
        print(href)
        pic_urls.append(href)

    return pic_urls

    # retrieves the source code for the given picture
    #  from the source code, gets the url of the original image (full-sized) on facebook's servers
def get_pic_page_source(pic_url):
    source = requests.get(pic_url)
    source = BeautifulSoup(source.content, 'html.parser')
    try:
        orig = source.find("meta", property="og:image")
        print(orig["content"])
        return orig["content"]
    except:
        print("Cant find original image")

    # saves the full-sized image locally.
def save_images(url_list, profile):
    for index, url in enumerate(url_list):
        if not os.path.exists(profile):
            os.mkdir(profile)
        img_name = "{0}_{1}".format(profile, index)
        path = os.path.join(profile, img_name)
        urllib.request.urlretrieve(url, path)
        print("Image saved as {0}.".format(path))

def main():
    profile = sys.argv[1]
    insta_url = 'https://www.instagram.com/{0}/'.format(profile)
    browser = load_full_browser_page(insta_url)
    pic_urls = get_pic_urls(browser)
    orig_pic_urls = []
    for pic in pic_urls:
        orig_pic_urls.append(get_pic_page_source(pic))
    save_images(orig_pic_urls, profile)
    

if __name__ == '__main__':
    main()
