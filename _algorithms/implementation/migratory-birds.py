#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    type_counts = {1:0, 2:0, 3:0, 4:0, 5:0}
    for bird_type in ar:
        type_counts[bird_type] += 1
            
    max_type = 0
    max_count = 0
    for bird_type in range(1,6): #this will do them in order, so it will only replace if strictly greater
        cur_count = type_counts[bird_type]
        if cur_count > max_count:
            max_type = bird_type
            max_count = cur_count
      
    return max_type  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

