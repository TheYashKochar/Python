# Sorts the Grade and Keeps the Best 2
print('Welcome to the Grade Sorter!')
grade=[]
g1 = input('Enter your first grade (0-100): ')
g2 = input('Enter your Second grade (0-100): ')
g3 = input('Enter your Third grade (0-100): ')
g4 = input('Enter your fourth grade (0-100): ')
grade.append(g1)
grade.append(g2)
grade.append(g3)
grade.append(g4)
print('Your Grades are : ',end='')
print(grade)
grade=grade.sort(reverse=True)
print('Your Sorted Grades are : ',end='')
print('Lowest 2 Grades will be droppped.\n')
print('Removing Grade :',end='')
#print(grade.pop())
grade.pop()
#print('Removing Grade :',end='')
print(grade.pop())
grade.pop()
print('Your Remaining Grades are :' ,end='')
print(grade)
print('Your Highest Grade is ',end='') 
print(grade[0])