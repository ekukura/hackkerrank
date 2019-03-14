#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(day):
    """
    :type day: int
    """
    
    day_str_arr = list(str(day))
    reversed_day_str_arr = reversed(day_str_arr)
    reversed_day = int("".join(reversed_day_str_arr))
    
    # reversed_day_arr = [int(char) for char in day_str_arr]
    # reversed_day = sum(reversed_day_arr[i]*pow(10,i) for i in range(len(reversed_day_arr)))
    return reversed_day

def isBeautiful(day, k):
    
    diff = abs(day - reverse(day))
    if diff % k == 0:
        return True
    else:
        return False

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    num_days = 0
    for day in range(i, j+1):
        if isBeautiful(day, k):
            num_days += 1
    
    return num_days

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')
    fptr.close()

