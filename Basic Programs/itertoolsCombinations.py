from itertools import combinations
a,b = input().split()
for x in range(1,int(b)+1):
    print(*[''.join(i) for i in combinations(sorted(a),x)],sep='\n')
'''
print(*sorted(a),sep='\n')
print(*[''.join(i) for i in combinations(sorted(a),int(b))],sep='\n')
'''