#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the misereNim function below.
def misereNim(s):
    # almost the same as regular Nim, can drive down, alternating CUMXOR parity
    # and once reduced to [2 2], -> [2,1] or [2] -> [1]
    # only special case is if all are 1's -- in this case winner depends 
    # on parity, since in this case have no choice but to end in 1 1
    # if all are ones, winner depends on parity
    sset = set(s)
    if sset == {1}: 
        if len(s) % 2 == 1:
            return "Second"
        else:
            return "First"
    else:
        cum = s[0]
        ind = 1
        while ind < len(s):
            cum = cum ^ s[ind]
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

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()

