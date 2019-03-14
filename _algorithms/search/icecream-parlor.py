#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    
    n = len(arr)
    res = None
    
    found = False
    i = 0
    
    while i < n and not found:
        cur_first = arr[i]
        target = m - cur_first 
        j = i+1
        while j < n and not found:
            if target == arr[j]:
                found = True
                res = (i+1, j+1)
            else:
                j += 1
        i += 1
    
    print(res[0], res[1])  
    return res    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

