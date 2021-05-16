# Program to format the unformatted images
import os
os.chdir('D:\\Project\\Python\\files\\test')
#print(os.listdir())
for filename in os.listdir():
    if not filename.endswith('.jpg'):
        os.rename(filename, filename + '.jpg')

print(os.listdir())
