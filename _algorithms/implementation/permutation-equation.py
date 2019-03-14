#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    
    n = len(p)
    inverse = dict()
    for i in range(1, n+1):
        inverse[p[i-1]] = i
    # inverse maps i -> p^(-1)(i)
        
    ys = [inverse[inverse[j]] for j in range(1,n+1)]
    return ys
    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

