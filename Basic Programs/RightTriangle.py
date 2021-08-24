# Finding Hypotenuse and Area of Right Angled Triangle
import math
print('Welcome to the Right Triangle Solver!')
leg1=input('Enter the First Leg of Triangle : ')
leg2=input('Enter the Second Leg of Triangle : ')
hypo=round(math.sqrt(math.pow(float(leg1),2)+math.pow(float(leg2),2)),3)
area=(float(leg1)*float(leg2))/2
print('Hypotenuse is '+str(hypo)+' and Area is '+str(area))