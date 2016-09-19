#!/usr/bin/python3
# Getting libraries
print ("MR.VIRUS32")
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Loading page
url = urlopen("http://ubuntuhandbook.org/")
# Geting last posts name
html = BeautifulSoup(url.read(), 'html.parser')
for web in html.find_all("h2"):
    print(web.get_text())
