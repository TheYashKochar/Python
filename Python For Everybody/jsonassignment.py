import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)
info = json.loads(urllib.request.urlopen(address).read())
print('User count:', len(info))
print(type(info))
ls=list()
total = 0
for item in info["comments"]:
    total += int(item["count"])

print(total)
