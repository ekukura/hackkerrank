#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the canConstruct function below.
def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    # Note a number is divisible by 3 iff the sum of its individual digits is
    # so - the actual rearrangement is irrelevant, just put them in order they arrive in
    digit_sum = 0
    for el in a:
        digits = [int(d) for d in str(el)]
        digit_sum += sum(digits)
        
    if digit_sum % 3 == 0:
        return "Yes"
    else:
        return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()

