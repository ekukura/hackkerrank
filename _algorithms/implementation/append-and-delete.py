#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # first get common substring starting at index 0
    shorter = s if len(s) <= len(t) else t
    longer = t if len(s) <= len(t) else s
    differ = False
    i = -1
    while not differ and i < len(shorter) - 1:
        i += 1
        if shorter[i] != longer[i]:
            differ = True
    if differ:
        common_sub = shorter[:i]
        shorter_rem = shorter[i:]
        longer_rem = longer[i:]
    else:
        common_sub = shorter
        shorter_rem = ''
        longer_rem = longer[i+1:] if i+1 < len(longer) else ''
        
    len_rem = len(shorter_rem) + len(longer_rem)
    if not common_sub:
        # '' + 'rank'
        # '' + 'dog'
        if k < len_rem:
            return 'No'
        else:
            return 'Yes'
    else:
        # e.g. 'hacker' + 'rank'
        #      'hacker' + 'dog'
        if k < len_rem:
            return 'No'
        else: # k >= len_rem
            if k >= len_rem + 2*len(common_sub): 
                # erase entire first string, 'delete' as many times as needed, then write other string
                return 'Yes'
            elif (k - len_rem) % 2 == 0:
                return 'Yes'
            else:
                return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    t = input()
    k = int(input())
    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')
    fptr.close()

