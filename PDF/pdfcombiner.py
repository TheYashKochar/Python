# Test Program to combine PDFs
import PyPDF4
print('imported')
file = open('meetingminutes1.pdf','rb')
file2 = open('meetingminutes2.pdf','rb')
reader1 = PyPDF4.PdfFileReader(file)
reader2 = PyPDF4.PdfFileReader(file2)
writer = PyPDF4.PdfFileWriter()
for pagenum in range(reader1.numPages):
    page = reader1.getPage(pagenum)
    writer.addPage(page)

for pagenum in range(reader2.numPages):
    page = reader1.getPage(pagenum)
    writer.addPage(page)

Output = open('Combined.pdf','wb')
writer.write(Output)
print('Combined')
Output.close()
file.close()
file2.close()
