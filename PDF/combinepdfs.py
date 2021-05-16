# Program to Combine the PDFs
import PyPDF4
num = int(input('Enter the number of Files to be Combined :'))
pdflist =[]
for x in range(num):
    filename = input('File Name : ')
    pdflist.append(filename)

print('The List of Files to be Combined:')
for z in pdflist:
    print(z)

writer = PyPDF4.PdfFileWriter()

for z in pdflist:
    file = open(z,'rb')
    reader1 = PyPDF4.PdfFileReader(file)
    for pagenum in range(reader1.numPages):
        page = reader1.getPage(pagenum)
        writer.addPage(page)

Output = open('Combined.pdf','wb')
writer.write(Output)
print('Combined')
Output.close()
file.close()
