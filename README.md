## InstaGrab

### What it does
The program takes one user input from the command line: a given Instagram profile name. It then finds all images on the page,
gets the url to the original hi-res image, and saves each image locally. 


### Motivation
When I upload a photo to Instagram, I usually delete it off my phone afterwords. 
When I go to download them again, they look compressed and blurry.
I discovered that a higher-resolution version of the image is saved on Facebook's servers and if you know the url, you can download it. It's slow to download each image manually, so I wanted to be able to download them all at once.

### Tools Used
The program is written in Python, and I used some of the following modules:
* Selenium - In particular the web driver to 'drive' the chrome browser page
* BeautifulSoup - Used to parse html content in this project
* requests and urllib.request to open urls

### How to use
1. Clone or download it somewhere
2. Install python, pip (package installer for python) & google chrome if you dont have them
3. Use _pip install -r requirements.txt_ to install the necessary packages
4. Run _python main.py "username"_ to download all the pictures.
5. The images saved in a directory with their username.
