# Program to extract Text from PDFs
import PyPDF4
print('imported')
a = input('File Name:')
file = open(a,'rb')
reader = PyPDF4.PdfFileReader(file)
#num = reader.numPages
for x in range(reader.numPages):
    #page = reader.getPage(x)
    print(reader.getPage(x).extractText())
