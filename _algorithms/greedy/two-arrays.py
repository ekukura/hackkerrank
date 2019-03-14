#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    increasing = sorted(A)
    decreasing = sorted(B, reverse=True)
    totals = [increasing[i] + decreasing[i] for i in range(len(A))]
    min_tot = min(totals)
    return "YES" if min_tot >= k else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()

