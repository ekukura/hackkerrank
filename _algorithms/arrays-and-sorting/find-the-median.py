#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
    n = len(arr) # e.g. if n = 5 median at element with ind 2
    arr.sort()
    midpoint = int((n-1)/2)
    return arr[midpoint]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)

    fptr.write(str(result) + '\n')
    fptr.close()

