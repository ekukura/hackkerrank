#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pokerNim function below.
def pokerNim(k, c):
    # convert each pile into its bit representation
    # XOR each bit
    # if every bit is 0, you are in a LOSING state
    # you are forced to break this on your next turn, and the opponent can then
    # force you back into it (and there are a lower total # of stones at that point)
    # eventually opponent will have to remove a pile (or if they leave you with XYZA where
    # XYZ would be a losing state, you can remove the 'A' pile yourself), giving you a 
    # winning state with less piles (resp., forcing them into a lower # of piles at the 
    # losing state)
    cum = c[0]
    ind = 1
    while ind < len(c):
        cum = cum ^ c[ind]
        ind += 1
    
    if cum == 0:
        return "Second"
    else:
        return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        c = list(map(int, input().rstrip().split()))

        result = pokerNim(k, c)

        fptr.write(result + '\n')

    fptr.close()

