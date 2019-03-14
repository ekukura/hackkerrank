#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chessboardGame function below.
def chessboardGame(x, y):
    """
    First player loses iff starts in (a,b), where
    a = (1 or 2) % 4 and b = (1 or 2) mod 4
    """
    
    losing_set = {1,2}
    if x % 4 in losing_set and y % 4 in losing_set:
        return "Second"
    else:
        return "First"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()

