

import urllib.request as urllib2
from bs4 import BeautifulSoup
import requests

arr = []
arr1 = []
page = 'https://en.wikipedia.org/wiki/History_of_India'
soup=BeautifulSoup(requests.get(page).text, 'lxml')
#soup=BeautifulSoup(p, 'html.parse

for h in soup.find_all(["h1", "h2", "h3", "h4", "h5"]):
    x = str(h.text.strip())
    arr.append(x)
    
x = ' '.join(arr)[0:150] + "..."
arr1.append(x)
print(arr1)

