from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))# *is the unpacking operator
'''
a = input().split()
b = input().split()
for x in range(len(a)):
    a[x]= int(a[x])
for x in range(len(b)):
    b[x]= int(b[x])    
z=list(product(a,b))
for x in z:
    print(x,end=' ')
'''
