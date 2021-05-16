# Program to Map a Location
import webbrowser
#import sys
#import pyperclip
'''
sys.argv
if len(sys.agrv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    #address = pyperclip.paste()
    address = input()
'''
address = input('Please Enter a place:\n')
webbrowser.open('https://www.google.com/maps/place/'+address)
