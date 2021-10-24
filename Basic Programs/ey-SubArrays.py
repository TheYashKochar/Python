def subarray(a,size):
    count = 0
    num = 0
    for i in a:
        for j in range(i,len(a)):
            num += a[j]
            
            if num == 0:
                print((i,j))



a = [1,-1,23,-22,40,-45,6]
size = len(a)
print(subarray(a,size))