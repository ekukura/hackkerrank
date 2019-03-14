#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    if (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):         
        res = "NO"
        
    else:
        '''
        At time t, the locations of k1 and k2 are: 
        
        k1: x1 + t*v1
        k2: x2 + t*v2
        
        For them to meet, for some non-negative integer t we must have:
        
            x1 + t*v1 = x2 + t*v2
            x1 - x2 = t * (v2 - v1)
            
            t = (x1 - x2) / (v2 - v1) 
            aka x1 - x2 must be a positive multiple of v2 - v1.
            
            We already checked in the if above that x1 - x2 / v2 - v1 
            will be positive, just remains to check it is an integer
            
            It will be if (x1 - x2) mod (v2 - v1) = 0
        '''
        if ((x1 - x2) % (v2 - v1) == 0):
            res = "YES"
        else:
            res = "NO"
        
    return(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

