# finding total file size
import os
totalSize = 0
for filename in os.listdir('D:\\Project\\Python'):
    if not os.path.isfile(os.path.join('D:\Project\Python','filename')):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('D:\Project\Python',filename))
print(totalSize)
