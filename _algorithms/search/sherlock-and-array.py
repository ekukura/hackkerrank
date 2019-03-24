#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    n = len(arr)
    if n == 1:
        return 'YES'
    else:
        # n >= 2
        # this is for index 0
        lsum = 0
        rsum = sum(arr[1:])
        found = (lsum == rsum)
        ind = 1
        while not found and ind < n:
            # when move from ind-1 to ind:
            # left moves from arr[:ind-2] to arr[:ind-1] and
            # right moves from arr[ind:] to arr[ind+1:]
            lsum += arr[ind-1]
            rsum -= arr[ind]
            found = (lsum == rsum)
            ind += 1
        
        return 'YES' if found else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        fptr.write(result + '\n')

    fptr.close()

