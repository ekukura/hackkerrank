#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    # convert each pile into its bit representation
    # XOR each bit
    # if every bit is 0, you are in a LOSING state
    # you are forced to break this on your next turn, and the opponent can then
    # force you back into it (and there are a lower total # of stones at that point)
    # eventually opponent will have to remove a pile (or if they leave you with XYZA where
    # XYZ would be a losing state, you can remove the 'A' pile yourself), giving you a 
    # winning state with less piles (resp., forcing them into a lower # of piles at the 
    # losing state)
    cum = pile[0]
    ind = 1
    while ind < len(pile):
        cum = cum ^ pile[ind]
        ind += 1
    
    if cum == 0:
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()

