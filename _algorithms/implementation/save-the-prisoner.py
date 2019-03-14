#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    """
    - n : the number of prisoners 
    - m : the number of sweets 
    - s : the chair number to start passing out treats at
    """
    target = ((s + (m-1)) % n) 
    if target == 0: 
        target = n
    return target
    # ex: s = 2, m = 4, n = 3 -- (s + m-1) % 3 = 5 = 2
    # ex. s = 2, m = 2, n = 3 -- (s + m-1) % 3 = 3 % 3 = 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for t_itr in range(t):
        nms = input().split()
        n = int(nms[0])
        m = int(nms[1])
        s = int(nms[2])
        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()

