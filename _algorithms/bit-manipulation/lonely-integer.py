#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    # create a set as go through a; remove element if see it again. At end should be exactly one remaining element, which is what you want.
    nums = set()
    for num in a:
        if num in nums:
            nums.remove(num)
        else:
            nums.add(num)
            
    return nums.pop()

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')
    fptr.close()

