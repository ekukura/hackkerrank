#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    '''
    Once we have appended a letter x to p, 'x' is a substring of p and so we can always add it again for free. Conversely if x is not in p, then we MUST append it for a charge of $1. So the minimum cost is exactly the number of unique letters.
    '''
    letters = set(s)
    return len(letters)

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        fptr.write(str(result) + '\n')

    fptr.close()

