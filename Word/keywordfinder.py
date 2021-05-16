# Program to find Important Keywords in a Word File
import docx,docs

def getText(filename,key):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        for x in range(len(para.runs)):
            if key == 'bold':
                if(para.runs[x].bold == True):
                    #print(para.runs[x].text)
                    fullText.append(para.runs[x].text)
            if key == 'italic':
                if(para.runs[x].italic == True):
                    #print(para.runs[x].text)
                    fullText.append(para.runs[x].text)
            if key == 'underline':
                if(para.runs[x].underline == True):
                    #print(para.runs[x].text)
                    fullText.append(para.runs[x].text)
            if key == 'all':
                if(para.runs[x].bold == True):
                    #print(para.runs[x].text)
                    fullText.append(para.runs[x].text)
                if(para.runs[x].italic == True):
                    #print(para.runs[x].text)
                    fullText.append(para.runs[x].text)
                if(para.runs[x].underline == True):
                    #print(para.runs[x].text)
                    fullText.append(para.runs[x].text)
        #fullText.append(para.text)
    return '\n'.join(fullText)

filename = input('Enter the Filename : ')
key = int(input('Find Text having :\n1.Bold\n2.italic\n3.underline\n4.All the above\nEnter the Number : '))
if key == 1:
    print(getText(filename,'bold'))
elif key == 2:
    print(getText(filename,'italic'))
elif key == 3:
    print(getText(filename,'underline'))
elif key == 4:
    print(getText(filename,'all'))
else:
    print('Please Input Number')
