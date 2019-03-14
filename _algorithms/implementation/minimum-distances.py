#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    # traverse the array, storing values and their most recent
    # index, and keeping track of the minimum dist
    # e.g. [1,3,5,3,1,5,5,7]
    min_dist = len(a) 
    info = dict()
    # {1:0, 3:1, 5:2}
    for ind in range(len(a)):
        val = a[ind]
        if val in info:
            #check the distance to most recent occurance
            dist = ind - info[val]
            if dist < min_dist:
                min_dist = dist
                
        info[val] = ind #update info dict w/ most recent ind
            
    return min_dist if min_dist < len(a) else -1

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)

    fptr.write(str(result) + '\n')
    fptr.close()

