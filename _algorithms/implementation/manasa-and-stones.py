#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    nz = n-1
    smaller = min(a,b)
    larger = max(a,b)
    possibilities_set = {k*larger+(nz-k)*smaller for k in range(nz+1)}
    return sorted(list(possibilities_set))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

