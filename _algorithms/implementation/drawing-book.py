#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    forward_flips = int(math.floor(p/2))
    
    bf_base = (n-p)/2
    backward_flips = int(math.ceil(bf_base) if n % 2 == 0 else math.floor(bf_base))
    
    return min(forward_flips, backward_flips)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

