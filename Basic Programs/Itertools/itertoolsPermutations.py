from itertools import permutations
a,b = input().split()
b=int(b)
z = list(permutations(a,b))
l=[]
for x in z:
    c = ''
    for y in x:
        c+=y
    l.append(c)

l.sort()
for x in l:
    print(x)

'''
Same code as above in two lines
a,b = input().split()
print(*[''.join(i) for i in permutations(sorted(a),int(b))],sep='\n')
'''