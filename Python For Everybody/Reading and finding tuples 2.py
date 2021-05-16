# Program to read file and find emails
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


counts = {}

for line in handle:
   if not line.startswith("From "):continue

   time = line.split()
   time = time[5]
   hour = time.split(':')
   hour = hour[0] 

   counts[hour] = counts.get(hour, 0) + 1


for k, v in sorted(counts.items()):

    print (k,v)