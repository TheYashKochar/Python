# Program to Find Phone Numbers
import re
message = input()
numRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(numRegex.findall(message))
