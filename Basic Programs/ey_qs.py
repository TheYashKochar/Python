/*
Array of n elements. 
Accept.
Print 3rd largest.
*/
def thirdlar(array):
	max = []
	for y in range(2):
		for x in array:
			if x>max and not in max:
				max.append(x)
		
		
	
	for z in array:
		if x>max:
			max=x
	
return max
/*
1,3,4
4

subarrays whose total = 0
No Bad Array Found
Count
piyush.tilloo@gds.ey.com

Code:*/
def subarrays(a,size):
    count = 0
    for i in range(size):
	num = 0
        for j in range(i, size):
            num += a[j]
            if num == 0:
                count +=1

    return count
 

a = [1,-1,23,-22,40,-45,5]
size=len(a)
print(subarrays(a,size))

/*
Approach:
First we will pass the array and size of the array to the Function and then 
first for loop will traverse in the range of the size, and then we initialize 'num' to zero which will be used to get the total of number 
then second for loop will be initialized which traverse in array elements and add it to the num variable and after the loop end
num will be check if the total is zero or not if it is zero then 'count' gets increment of 1.

count -> it is the count of total no. subarrays having zero
num -> it is a temporary variable created to check the total of the values in the array
a -> It is the array
subarray -> Function Name
size -> Length of the Array

*/


















	


	