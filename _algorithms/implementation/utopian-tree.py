#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    
    if n % 2 == 0:
        k = int(n/2)
        h = int(math.pow(2,k+1)) - 1
        
    else:
        k = int((n-1)/2)
        h = 2*(int(math.pow(2,k+1)) - 1)
        
    return h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

