#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    
    max_val = 0
    for v1 in range(l, r):
        for v2 in range(v1 + 1, r+1): # a xor a = 0 always
            cur = v1 ^ v2
            if cur > max_val:
                max_val = cur
                
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()

