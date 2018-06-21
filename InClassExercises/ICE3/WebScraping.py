
import urllib.request
from bs4 import BeautifulSoup
import os
import requests

# get data on the CYP2D6 gene
url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#html =  urllib.request.urlopen(url).read().decode('utf-8')
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

# find title
title = soup.findAll('title')
print(title)

# get all <div> content and then print content for any headers
for div in soup.find_all('a'):
    aTag = div.get('href')

    # not all divs have h1 so only print if there is something to print
    if aTag != None :
        print(aTag)

# print the full text of the body -- note that this include embedded javascript
#print(soup.get_text())