#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    
    s = list(s)
    min_removals = 0
    while len(s) > 0:
        empty = False
        #each iteration, get top char and remove any that are the same following
        back_char = s.pop()
        try:
            next_char = s[-1]
        except IndexError:
            empty = True

        while (next_char == back_char) and (not empty): #if in the same contiguous streak of 'back_char''s
            s.pop() # pop off next_char
            min_removals += 1
            try:
                next_char = s[-1]
            except IndexError:
                empty = True
            
    return min_removals

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

