# Program to crawl through a certain folder
import os
os.chdir('D:\\')
for folderName, subfolders, filesname in os.walk(os.getcwd()):
    print('The folder is :' + folderName)
    print('Subfolders are :' + str(subfolders))
    print('The Files are :' + str(filesname))
    print()

    '''
    for subfolder in subfolders:
        if 'asmdksakdadsadadasdsad' in subfolder:
            os.rmdir(subfolder)
    '''
