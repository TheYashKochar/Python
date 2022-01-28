# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
avg=0
a=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
        f=line.find('0')
        z=float(line[f:])
        a=a+z
avg=a/count
print("Average spam confidence:" , avg)
