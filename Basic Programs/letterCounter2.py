# Counting the Letters in a Text Method 2
print('Welcome to the Letter Counter!')
name = input('What is your name ?\n')
print('Hey! '+name+' This Program will count occurences of a Letter in the text provided by you.')
text=input('Enter the Text : ')
letter=input('Enter the Letter to be counted : ')
text=text.lower()
letter=letter.lower()
count=text.count(letter)

print('Letter \'' + letter + '\' Occurs ' + str(count) + ' times.')
