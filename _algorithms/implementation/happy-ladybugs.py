#!/bin/python3

import math
import os
import random
import re
import sys

def is_happy(b):
    last = b[0]
    ind = 1
    while ind < len(b): 
        cur = b[ind]
        if cur == '_':
            last = cur
            ind += 1
        else:
            future = b[ind+1] if ind < len(b) - 1 else ''
            if cur != last and cur != future:
                return False
            elif cur == future:
                last = cur
                ind += 2
            else:
                last = cur
                ind += 1
    return True

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    # if there's at least one underscore and at least 
    # two ladybugs of each color, can win
    # otherwise if there's no underscore only win if initial
    # position good

    counts = dict()
    for item in b:
        counts[item] = counts.get(item, 0) + 1

    underscore_count = counts.pop('_', 0)
 
    if not counts:
        return 'YES'
    
    else:
        min_color_count = min(counts.values()) 
        if min_color_count == 1:
            return 'NO'
        else: # at least 2 of each ladybug
            if underscore_count >= 1:
                return 'YES'
            else:
                # since no underscores, need to check if already happy
                happy_as_is = is_happy(b)
                return 'YES' if happy_as_is else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

