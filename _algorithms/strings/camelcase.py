#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.

def is_upper_case(char):
    
    if char in {"A", "B", "C", "D","E","F","G","H","I",
                "J","K", "L","M","N","O","P","Q","R",
                "S","T","U","V","W","X","Y","Z"}:
        return True
    else:
        return False


# Complete the camelcase function below.
def camelcase(s):
    if len(s) == 0:
        return 0
    else:
        num_words = 1
        for i in range(1, len(s)):
            if is_upper_case(s[i]):
                num_words += 1
                
        return num_words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

