#!/bin/python3

import math
import os
import random
import re
import sys

def isOdd(x):
    return True if x % 2 == 1 else False
    
# Complete the fairRations function below.
def fairRations(B):
    dist = 0
    if isOdd(sum(B)):
        return "NO"
    else:
        i = 0
        # traverse array, flipping parity as go; 
        while i < len(B) - 1:
            if isOdd(B[i]):
                B[i] += 1
                B[i+1] += 1
                dist += 2
            i += 1
                
    return dist  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)

    fptr.write(str(result) + '\n')
    fptr.close()

