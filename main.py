import os
import urllib3
import urllib.request
import requests
from http.client import HTTPConnection


from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


url = "https://www.instagram.com/p/Bs-_Cqvnm6Z/"
cont = requests.get(url)
soup = BeautifulSoup(cont.content, 'html.parser')

image_src = soup.find("meta", property="og:image")
print(image_src["content"] if image_src else "Cant find original image")


#TODO need a web driver or selenium or something

sam_url = 'https://www.instagram.com/samwluby/'
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(sam_url)

print(browser.find_element_by_class_name('FyNDV').text)


# insta_url = 'www.instagram.com/'
# conn = HTTPConnection(insta_url)
# conn.request("GET", "samwluby")
# print(conn.getresponse().read())



# html = urllib.request.urlopen(sam_url)
# soup = BeautifulSoup(html)
# print(soup)
# f = urllib.request.urlopen(url)
# html = f.read()s
# html_new = html.decode('utf8')
# print(html_new)
# print(html)
# html = urllib.request.urlopen(url)
# soup = BeautifulSoup(html, 'html5lib')

# soup = BeautifulSoup(cont.content, 'html5lib')
# imgs = soup.find_all("div")
# print(imgs)
# row_of_images_id = 'Nnq7C weEfm'
# images = soup.find_all("v1Nh3 kIKUG  _bz0w")
# imgs = []
# divs = soup.find_all('div', attrs={'class': 'v1Nh3 kIKUG  _bz0w'})
# for div in divs:
#     if div["class"] == "v1Nh3 kIKUG  _bz0w":
#         imgs.append(div)
# print(imgs)
# print(divs)
