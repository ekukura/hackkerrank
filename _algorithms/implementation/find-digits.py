#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    
    str_n_arr = list(str(n))
    digits = [int(char) for char in str_n_arr]
    n_div = 0
    for d in digits:
        if (not d == 0) and (n % d == 0):
                n_div += 1
            
    return n_div

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

