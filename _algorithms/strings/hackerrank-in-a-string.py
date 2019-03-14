#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    
    hackerrank_stack = ["k", "n", "a", "r", "r", "e", "k", "c", "a", "h"]
    s_ind = 0
    while len(hackerrank_stack) > 0 and s_ind < len(s):
        if s[s_ind] == hackerrank_stack[-1]:
            hackerrank_stack.pop()
        s_ind += 1
        
    if len(hackerrank_stack) > 0:
        return "NO"
    else:
        return "YES"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

