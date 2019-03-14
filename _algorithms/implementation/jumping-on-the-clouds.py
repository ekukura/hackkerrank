#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    n = len(c)
    
    num_jumps = 0
    cur_location = 0
    
    #if haven't yet reached the last cloud, keep jumping
    while cur_location < n-1: 
        #check if can jump two. if so do this, otherwise jump 1
        if cur_location + 2 <= n-1:
            if c[cur_location + 2] == 0:
                cur_location += 2 #jump 2
            else: 
                cur_location += 1 #jump 1
        else:
            #otherwise since no two consec. 1's, next location open
            cur_location += 1 
            
        num_jumps += 1
        
    return num_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

