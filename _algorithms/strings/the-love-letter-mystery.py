#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    """
    :type s: str 
    """
    num_changes = 0
    s_arr = list(s)
    n = len(s)
    even = (n % 2 == 0)
    
    last_compare_index = int(n/2)-1 if even else int((n-1)/2) - 1
    for ind in range(last_compare_index+1):
        # trip 'smaller' of pair
        former = s_arr[ind]
        latter = s_arr[-(ind+1)]
        num_changes += abs(ord(former) - ord(latter))
    
    return num_changes

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        fptr.write(str(result) + '\n')

    fptr.close()

