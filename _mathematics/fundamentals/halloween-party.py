#!/bin/python3

import os
import sys

#
# Complete the halloweenParty function below.
#
def halloweenParty(k):
    #
    # Write your code here.
    #
    #
    # k = h + v (h=horiz; v=vert)
    #   = h*v pieces --> maximized when h~v
    # if k = 2*n cuts:
    # do n horizontal; n vertical
    #   -> n^2 pieces
    # else if k = 2*n + 1 do n horiz; n+1 vert 
    #   - > n(n+1) pieces
    if k % 2 == 1:
        n = int((k-1)/2)
        return n*(n+1)
    else:
        n = int(k/2)
        return n*n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for t_itr in range(t):
        k = int(input())
        result = halloweenParty(k)
        fptr.write(str(result) + '\n')

    fptr.close()

