# Program to find sum of the numbers in a file
import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_884502.txt"
handle = open(name)
count=0
lst=list()
for line in handle:
    line=line.strip()
    x=re.findall("[0-9]+",line)
    lst.append(x)
    #lst=re.findall("[aeiou]+",line)
lst = [ele for ele in lst if ele != []]
for x in lst:
    for y in x:
        count+=int(y)
#print(lst)
print(count)
