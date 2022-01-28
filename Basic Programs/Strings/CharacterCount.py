# Program to count characters in a string
import pprint
#message = 'Quick Brown Fox Jumps Over a lazy dog'
message = input('Please Give Input:')
count ={}

for character in message.upper():
    count.setdefault(character,0)
    count[character] += 1
#print(count)
pprint.pprint(count)

#text = pprint.pformat(count)
#print(text)
