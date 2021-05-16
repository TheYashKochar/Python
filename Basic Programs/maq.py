inputstring = input().split()
l = len(inputstring)
for x in inputstring:
 z= l-x
 while(z.isalpha() and x.isalpha()):
	 if(x.isalpha() and z.isalpha()):
   		temp= inputstring[l-x]
   	  inputstring[l-x]= inputstring[x]
      inputstring[x] = temp
 do:
  if(x.isalpha()):
     z=l-x-1
  else:
     x+=1
print(inputstring)
