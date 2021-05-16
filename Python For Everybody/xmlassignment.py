# XML Assignment from 'Python for Everybody Specialization'
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx).read()

#data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(uh)
#root = tree.getroot()
'''results = tree.findall('commentinfo/comments/comment/count')
lst = tree.findall('.//count')
bsd = tree.findall('comment')
#print(tree.find('.//count').text)
#print(results)
#print(lst)
z=list()
for x in lst:
    z.append(tree.find('.//count').text)
#print(z)
for item in bsd:
    print(item.find('count'))'''
total = 0
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        total += int(comment.find('count').text)

print(total)
