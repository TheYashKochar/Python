# importing required modules
from zipfile import ZipFile
import os

file_name = os.listdir()
#print(file_name)

for x in file_name:
    if x.endswith('.zip'):
        with ZipFile(x, 'r') as zipObj:
            listOfFileNames = zipObj.namelist()
            for fileName in listOfFileNames:
                if fileName.endswith('.wav'):
                    print('Extracting ' + x)
                    zipObj.extract(fileName, 'audio_data')

print('Done!')



'''
if x in file_name.endswith('.zip'):    
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(x, 'r') as zipObj:
    # Get a list of all archived file names from the zip
        listOfFileNames = zipObj.namelist()
    # Iterate over the file names
        for fileName in listOfFileNames:
            # Check filename endswith csv
            if fileName.endswith('.wav'):
                # Extract a single file from zip
                zipObj.extract(fileName, 'audio_data')

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
	# printing all the contents of the zip file
	zip.printdir()
	# extracting all the files
	print('Extracting all the files now...')
	zip.extractall()
	print('Done!')
'''