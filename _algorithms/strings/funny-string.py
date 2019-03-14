#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the funnyString function below.
def funnyString(s):
    diffs = [abs(ord(s[i+1])-ord(s[i])) for i in range(len(s)-1)]
    diffs_rev = copy.copy(diffs)
    diffs_rev.reverse()
    if diffs == diffs_rev:
        return "Funny"
    else:
        return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')

    fptr.close()

