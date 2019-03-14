#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    # e.g. a = [1,2,3,8,9], k = 3 -> [3,8,9,1,2]
    rotated_array = []
    n = len(a)
    k = k % n
    # now k < len(a)
    for i in range(n):
        # index through new array, finding the corresponding element
        # in the original array and appending it
        old_pos = (i-k) % n
        rotated_array.append(a[old_pos])

    res = [rotated_array[q] for q in queries]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

