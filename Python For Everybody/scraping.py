# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst=list()
# Retrieve all of the Span tags
tags = soup('span')
for tag in tags:
    #print(tag.get('class', None))
    #print(tag.contents[0])
    lst.append(tag.contents[0])

#Adding All the data
cnt=0
for x in lst:
    cnt+= int(x)
print(cnt)
