#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    # in bitwise rep of n, count number of 0s (z)
    # then 2^z is answer

    if n == 0:
        return 1
    else:
        bitn = "{0:b}".format(n)
        z = sum(1 for i in bitn if i == '0')
        return pow(2,z) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    result = sumXor(n)

    fptr.write(str(result) + '\n')
    fptr.close()

