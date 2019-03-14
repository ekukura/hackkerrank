#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    r = n % l
    # num complete occurences of s
    full_rounds = int((n-r)/l)  
    na = sum(1 if ch == "a" else 0 for ch in s)
    na_r = sum(1 if ch == "a" else 0 for ch in s[:r])
    res = na*full_rounds + na_r
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

