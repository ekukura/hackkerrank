#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sorted_toys = sorted(prices)
    total = 0
    n_toys = 0
    next_toy = sorted_toys[0]
    while total + next_toy <= k:
        total += next_toy
        n_toys += 1
        next_toy = sorted_toys[n_toys]
    return n_toys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')
    fptr.close()

