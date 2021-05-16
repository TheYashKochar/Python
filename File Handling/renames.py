# Program to rename the desired multiple files
import os,re,shutil
#os.chdir('')
#print(os.listdir())
#ls=[]
for filename in os.listdir():
    if not re.findall("[.]+",filename):
        if os.path.isfile(filename):
            #ls.append(filename)
            os.rename(filename, filename + '.jpg')
            #shutil.move(filename, 'conv')

#print(ls)
print('Converted')
