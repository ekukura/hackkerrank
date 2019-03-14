#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases, width):
    
    res_arr = [min(width[case[0]:case[1]+1]) for case in cases]
    
    # res_arr = []
    # for case in cases: #case e.g. [1,4]
    #     entry = case[0]
    #     exit = case[1]
    #     max_car_len = min(width[entry:exit+1])
    #     res_arr.append(max_car_len)
        
    return res_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nt = input().split()
    n = int(nt[0])
    t = int(nt[1])
    width = list(map(int, input().rstrip().split()))
    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

