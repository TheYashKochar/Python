# Program to Find Phone Numbers in a Text
import re
message = input()
numRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobject = numRegex.search(message)
print(matchobject.group())
