#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s, d, m):
    n = len(s)
    if m > n:
        return 0
    else:
        counter = 0
        #looks at all m-length segments starting from 1'st square up to n-m-th square
        first_sum = sum(s[0:m])
        #print("sum 0: ", first_sum)
        if first_sum == d:
            counter += 1
            
        prev_sum = first_sum
        for start_square in range(1, n-m+1): 
            cur_sum = prev_sum - s[start_square-1] + s[start_square + m - 1]
            #print("sum ", start_square , ": " , cur_sum)
            if cur_sum == d:
                counter += 1
            prev_sum = cur_sum
        
        print(counter)
        return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

