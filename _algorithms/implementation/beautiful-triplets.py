#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    # arr sorted array, d desired difference
    # O(1) pass through to determine number of each
    freq = dict()
    for val in arr:
        freq[val] = freq[val] + 1 if val in freq else 1
   
    # print("freq: {}\n".format(freq))
    num_triplets = 0
    for start_num in freq:
        # let s = start_num
        # target sequence s, s+d, s+2d
        first = freq.get(start_num, 0)
        second = freq.get(start_num + d, 0)
        third = freq.get(start_num + 2*d, 0)
        n_curr_triplets = first*second*third
        # print(start_num, first, second, third, n_curr_triplets)
        num_triplets += n_curr_triplets
            
    return num_triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')
    fptr.close()

