# Program to extract Text from '.docx' files
import docx,docs

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

a = 'demo.docx'
print(getText(a))
