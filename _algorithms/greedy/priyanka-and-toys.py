#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    # start with 1 box holding the first item
    lightest_item = w[0]
    containers = 1
    cur_ind = 1
    while cur_ind < len(w):
        if w[cur_ind] > lightest_item + 4:
            # start a new box
            containers += 1
            lightest_item = w[cur_ind]

        cur_ind += 1

    return containers       
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)

    fptr.write(str(result) + '\n')
    fptr.close()

