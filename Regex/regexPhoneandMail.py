#! Python 3
# Program to Find numbers and mails
import re, pyperclip
# regex for phone number
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\d)))? #area code
(\s-) # separator
\d\d\d # 3 digit
- # separator
\d\d\d\d # 4 digit
((ext(\.)?\s)|x  #extension word part
(\d(2,5)))? #extension number part
) # one large group to remove tuples
''',re.VERBOSE)
# regex for email
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ # @symbol
[a-zA-Z0-9_.+]+ # domain part
''',re.VERBOSE)
# getting text from clipboard
text = pyperclip.paste()
# extraction
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phn in extractedPhone:
    allPhoneNumbers.append(phn[0])

# DEBUG
'''print(extractedPhone)
print(extractedEmail)'''

# results
results= '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
