#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    
    sorted_arr = []
    max_val = 100
    val_counts = [0 for _ in range(max_val)]
    for val in arr:
        val_counts[val] += 1
        
    for i in range(max_val):
        sorted_arr.extend([i for _ in range(val_counts[i])])
        
    return sorted_arr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

