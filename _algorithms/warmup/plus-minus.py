#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    n = len(arr)
    num_positive = 0
    num_zero = 0
    num_negative = 0
    
    for i in range(n):
        if arr[i] > 0:
            num_positive += 1
        elif arr[i] == 0:
            num_zero += 1
        else:
            num_negative += 1

    print("{0:.6f}".format(num_positive/n))
    print("{0:.6f}".format(num_negative/n))   
    print("{0:.6f}".format(num_zero/n))
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

