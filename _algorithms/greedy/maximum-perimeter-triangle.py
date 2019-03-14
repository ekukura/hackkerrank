#!/bin/python3

import math
import os
import random
import re
import sys

def has_triangle(max_side, rem_sticks):
    # return -1 if no triangle else return the triangle with max side given
    l = len(rem_sticks)
    # let max_side = a. then is triangle if exist b,c in rem_sticks s.t. b+c>a
    # note b/c original sticks sorted in decreasing order, guaranteed that b,c < a individually
    sec_ind = 0
    triangle = None
    
    while sec_ind < l - 1 and not triangle:
        sec_side = rem_sticks[sec_ind]
        ## find if triangle with max_side, sec_side, x
        third_ind = sec_ind + 1
        while third_ind < l and not triangle:
            if sec_side + rem_sticks[third_ind] > max_side:
                triangle = [rem_sticks[third_ind], sec_side, max_side]
            third_ind += 1
        #######
        sec_ind += 1
        
    return triangle
    
# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    n = len(sticks)
    sticks.sort(reverse=True)
    # want max perimeter, so start with max lengths and decrease
    first_ind = 0
    triangle = None
    while first_ind < n - 2 and not triangle:
        triangle = has_triangle(max_side=sticks[first_ind], rem_sticks=sticks[first_ind+1:])
        first_ind += 1
    
    return triangle or [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

