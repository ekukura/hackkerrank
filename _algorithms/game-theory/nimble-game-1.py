#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimbleGame function below.
def nimbleGame(s):
    nim_piles = [i for i in range(len(s)) if s[i] % 2 == 1]
    
    cum = 0
    ind = 0
    while ind < len(nim_piles):
        cum = cum ^ nim_piles[ind]
        ind += 1
    
    if cum == 0:
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        s = list(map(int, input().rstrip().split()))
        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()

