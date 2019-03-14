#!/bin/python3

import math
import os
import random
import re
import sys

# Day Shared Liked Cumulative
# 1      5     2       2
# 2      6     3       5
# 3      9     4       9
# 4     12     6      15
# 5     18     9      24

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    
    total = 0
    start_shared = 5
    cur_shared = start_shared
    for i in range(1,n+1):
        cur_liked = int(math.floor(cur_shared/2))
        total += cur_liked
        cur_shared = 3 * cur_liked
        
    return total
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

