#!/bin/python3

import math
import os
import random
import re
import sys

# naive solution
def minimumAbsoluteDifference1(arr):
    n = len(arr)
    min_diff = pow(10,10) #max possible diff is 10^9 - (-10^9) = 2*10^9
    for first in range(n-1):
        for second in range(first+1, n):
            cur = abs(arr[second] - arr[first])
            if cur < min_diff:
                min_diff = cur
                
    return min_diff

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    n = len(arr)
    arr.sort()
    # min diff must be in neighbors
    min_diff = abs(arr[0] - arr[1])
    for ind in range(1, n-1):
        cur = abs(arr[ind+1] - arr[ind])
        print("CUR = {}".format(cur))
        if cur < min_diff:
            min_diff = cur
                
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()

