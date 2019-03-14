#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    wrappers = 0
    bars_eaten = int(math.floor(n/c))
    wrappers += bars_eaten
    while wrappers >= m:
        # trade in m wrappers for 1 bar
        wrappers -= m
        # eat bar
        bars_eaten += 1
        wrappers += 1

    return bars_eaten
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])

        result = chocolateFeast(n, c, m)
        fptr.write(str(result) + '\n')

    fptr.close()

