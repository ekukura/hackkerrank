#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 == 1:
        return -1
    else:
        l = int(len(s)/2)
        word1 = list(s[:l])
        word2 = list(s[l:])

        word1_count = dict()
        for c in word1:
            word1_count[c] = word1_count.get(c,0) + 1

        diff_char_count = 0
        for c2 in word2:
            if word1_count.get(c2, 0) > 0:
                word1_count[c2] -= 1
            else:
                # diff character
                diff_char_count += 1
        
        return diff_char_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')

    fptr.close()

