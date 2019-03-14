#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # to determine if contain common substring,
    #  enough to determine if contain a common letter
    letters_1 = set(s1)
    letters_2 = set(s2)
    inter = set.intersection(letters_1, letters_2)
    
    if inter:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

