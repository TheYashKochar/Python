# Program to calculate total size of files in a certain folder
import os
totalSize = 0
'''
for filename in os.listdir():
    print(os.path.join(os.getcwd(),filename))
'''
for filename in os.listdir():
    if not os.path.isfile(os.path.join(os.getcwd(), filename)):
        continue
    totalSize = totalSize + os.path.getsize(filename)
print(totalSize)
