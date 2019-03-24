#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    # always swap highest into next slot
    # elements of arr are a permutation (1..n)
    n = len(arr)
    if k >= n-1:
        return [i for i in range(n,0,-1)]

    # go through once and index all elements, then don't have to search
    locations = dict()
    for i in range(n):
        locations[arr[i]] = i

    ind = 0
    while k > 0 and ind < n:
        # find the value n-ind (ind+1-th largest)
        if arr[ind] != n-ind:
            # swap -- otherwise leave in place and move on
            swap_ind = locations[n-ind]
            tmp = arr[ind]
            arr[ind] = n-ind
            arr[swap_ind] = tmp
            # update locations
            locations[n-ind] = ind # don't actually care 
            locations[tmp] = swap_ind
            # decrement num swaps remaining
            k -= 1

        ind += 1

    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

