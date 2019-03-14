#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    left = []
    equal = []
    right = []
    
    # partition
    for el in arr:
        if el < p:
            left.append(el)
        elif el == p:
            equal.append(el)
        else:
            right.append(el)
    
    # put back together
    left.extend(equal)
    left.extend(right)
    
    return left

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

