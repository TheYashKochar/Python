# Program to Find Emails and generate tuples
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
for line in handle:
    line=line.strip()
    if not line.startswith("From: "):continue
    #line.rstrip()
    #w=line.split()
    #e=w[5]
    #e=w.split(":")
    #line.rstrip()
    hour = line.split()[5].split(':')[0]
    lst.append(hour)
 
#print(lst)        
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

#print(counts)
tmp=list()
for k,v in counts.items():
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)

tmp=sorted(tmp,reverse=True)
#print(tmp[:2])
for v,k in tmp[:3]:
    print(k,v)