sentences = []
question = ['What','How','When','Why','Can']
string=''

while string != '\end':
    string=input('Say Something : ')
    if string != '\end':
        if str.capitalize(string.split()[0]) in question:
            sentences.append(string.capitalize()+' ?')
        else:
            sentences.append(string.capitalize()+'.')

print(sentences)