#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    left_right_sum = 0
    right_left_sum = 0
    n = len(arr)
    for i in range(n): 
        cur_row = arr[i]
        '''
        for row i:
            for LTR sum want to add element i
            for RTL sum want to add element n-1-i
        '''
        left_right_sum += cur_row[i]
        right_left_sum += cur_row[n-1-i]
    
    diff = abs(left_right_sum - right_left_sum)
    
    return diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

