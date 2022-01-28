#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    capitalized_words = [w.capitalize() for w in words]
    return " ".join(capitalized_words)
    '''
    z=s.split()
    s=''
    for x in z:
        s+=' '+x.capitalize()
        print(x)
    
    #s=''
    #for x in z:
    #   s+=' '+x 
    #s[0] = s[0].upper
    #s[1] = s[1].upper
    return string.capwords(s,'')#s.strip()#.capitalize()'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
