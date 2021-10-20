# Printing Multiples and Exponents of a Number
print('Welcome to the Multiplication and Exponents Finder!')
num=float(input('Enter the Number : '))
print('Multiplication Table For '+ str(num))
for x in range(1,11):
    z=round(x*num,2)
    print(str(x) +' * '+ str(num) +' = '+ str(z))
print('Exponent Table For '+ str(num))
for x in range(1,11):
    print(str(x) +'**'+ str(num) +' = '+ str(round(x**num,2)))