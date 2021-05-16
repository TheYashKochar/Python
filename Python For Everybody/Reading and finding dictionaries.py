# Program Reading File and Finding Data
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
for line in handle:
    line=line.strip()
    if not line.startswith("From: "):continue
    #line.rstrip()
    w=line.split()
    e=w[1]
    #line.rstrip()
    lst.append(e)
 
#print(lst)        
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1
            
#print(counts)
word=None
val=-1
for k,v in counts.items():
    if v > val:
        val = v
        word = k
        #print(k,v)
       
print(word,val)
    
            