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
count = int(input('Enter Count - '))
pos = int(input('Enter Position - '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst=list()
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    lst.append(tag.get('href', None))
for x in range(count):
    html = urllib.request.urlopen(lst[pos], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst.clear()
    if x == count-1:
        for tag in tags:
            lst.append(tag.contents[0])
    else:
        for tag in tags:
            lst.append(tag.get('href',None))
        #lst.append(tag.contents[0])
print(lst)
'''for x in range(0,3):
    if x == 2:
        link=urllib.request.urlopen(lst[])'''
