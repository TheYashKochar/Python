import re
name = input("Enter file:")
if len(name) < 1 : name = "marks.txt"
handle = open(name)
lst=list()
for line in handle:
    line=line.strip()
    lst=re.findall("[0-9]*",line)

print(lst)
