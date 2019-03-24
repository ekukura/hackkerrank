#!/bin/python3

import math
import os
import random
import re
import sys

def powerSumHelper(X,N,m):
    # return number of unique combinations {k_i} s.t.
    # sum(k_i ^ N) = X and k_i <= m for all i
    # print("X = {}\tN={}\tm={}\n".format(X,N,m))
    if X == 0 and m >= 0:
        # print("returning 1")
        return 1

    elif sum(pow(i, N) for i in range(1, m+1)) < X:
        # print("returning 0")
        return 0

    else:
        counter = 0
        max_val = min(math.floor(pow(X, 1/N)), m)
        for i in range(max_val):
            count = powerSumHelper(X-pow(i+1,N),N,i)
            counter += count
        # print("returning {}".format(counter))
    return counter

# Complete the powerSum function below.
def powerSum(X, N):
    # print("X = {}\tN={}\n".format(X,N))
    counter = 0
    max_val = math.floor(pow(X, 1/N))
    # could optimize so only even try i large enough s.t.
    # i+1 COULD be the max component value (e.g. so don't)
    # have to do test at beginning of helper
    for i in range(max_val):
        count = powerSumHelper(X-pow(i+1,N),N,i)
        counter += count

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())
    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')
    fptr.close()

