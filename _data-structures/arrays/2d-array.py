#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def sum_individual_hourglass(start_i, start_j, arr):
    
    my_sum = sum(arr[start_i][start_j:start_j + 3])
    my_sum += arr[start_i + 1][start_j + 1]
    my_sum += sum(arr[start_i + 2][start_j:start_j + 3])
    
    return my_sum
    

def hourglassSum(arr):
    
    max_sum = -9*7 #min possible value since each entry b/w -9 and 9
    for i in range(4):
        for j in range(4):
            cur_sum = sum_individual_hourglass(i, j, arr)
            if cur_sum > max_sum:
                max_sum = cur_sum
    
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

