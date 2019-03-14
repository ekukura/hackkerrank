#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    # palindrome iff <=1 char has odd # occurences
    char_parity = dict()
    # store 0 if even parity; 1 if odd
    for c in s:
        if c in char_parity:
            char_parity[c] = (char_parity[c] + 1) % 2
        else:
            char_parity[c] = 1
        
    # if sum values <= 1 then can be rearranged into palindrome
    total = sum(char_parity.values())
    res = "YES" if total <= 1 else "NO"
    return res

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = gameOfThrones(s)

    fptr.write(result + '\n')
    fptr.close()

