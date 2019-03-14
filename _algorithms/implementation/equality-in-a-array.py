#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
        
    n = len(arr)
    counts = dict()
    for val in arr:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    
    max_occur = max(counts.values())
    return n - max_occur

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')
    fptr.close()

