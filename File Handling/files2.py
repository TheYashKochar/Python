# Program to read and write text on a '.txt' file
fname = input('Enter File Name : ')
#ReadFile = open('text.txt','a')
ReadFile = open('text.txt','a')
#ReadFile = open('text.txt')
#print(ReadFile.read())
#ReadFile.close()
#print(ReadFile.readlines())
ReadFile.write('\n ndsandnsandsnadnsandnsandnsadnsna')
ReadFile.close()
ReadFile = open('text.txt')
print(ReadFile.read())