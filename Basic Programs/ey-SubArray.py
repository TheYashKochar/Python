def subarrays(a,size):
    count = 0
    for i in range(size):
        total = 0
        for j in range(i, size):
            total += a[j]
            if total == 0:
                count +=1

    return count
 

a = [1,-1,23,-22,40,-45,5]
size=len(a)
print(subarrays(a,size))