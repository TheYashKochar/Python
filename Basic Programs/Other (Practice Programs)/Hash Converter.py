# Program to Convert Integer to Hash
a=int(input())
ls=input().split()
ls = map(int, ls)
t=tuple(ls)
print(hash(t))