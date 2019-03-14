#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    # min of bc, wc has associated cost b*bc or w*wc
    # other has cost b*min(bc, wc+z) or w*(min(wc, bc+z))
    cost = b*min(bc, wc+z) + w*min(wc, bc+z)
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bw = input().split()
        b = int(bw[0])
        w = int(bw[1])

        bcWcz = input().split()
        bc = int(bcWcz[0])
        wc = int(bcWcz[1])
        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)
        fptr.write(str(result) + '\n')

    fptr.close()

