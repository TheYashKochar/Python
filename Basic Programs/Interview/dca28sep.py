a=input()
b=[i for i in a if not i.isnumeric()]
#print(b)
c=[i for i in b if i.isalpha()]
#print(c)
d=[i for i in b if not i.isalnum()]
#print(d)
e=c+d
for x in e:
    print(x,end='')
'''
for x in a:
    if x.isalpha == True:
        print(x)
        b.append(x)

for x in a:
    if not x.isalnum:
        b.append(x)

print(b)
c=[]
for x in b:
    if x.isalpha:
        c.append(x)

print(c)
'''