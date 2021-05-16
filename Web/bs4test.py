# Program to Find Text from HTML
from bs4 import BeautifulSoup
f = input('Enter File Name : ')
w = open(f)
print(w)
#print(w.read())
soup = BeautifulSoup(w, 'lxml')
#print(soup.prettify())
#tags = soup.find('span')
tags = soup.find_all('div')
#tags = soup.find_all('div', class_ = 'title')
#print(tags)
for c in tags:
    print(c.text.replace(' ',''))
