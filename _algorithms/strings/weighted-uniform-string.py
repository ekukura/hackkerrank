#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    i = 1
    current_char = s[0]
    current_substr = current_char
    subs = set()
    while i < len(s):
        next_char = s[i]
        if next_char == current_char:
            current_substr += current_char
        else:
            subs.add(current_substr)
            current_char = next_char
            current_substr = current_char    
        i += 1
    subs.add(current_substr)
    
    vals = set()
    for sub in subs:
        cval = ord(sub[0]) - 96
        vals = vals.union({m*cval for m in range(len(sub) + 1)})

    res = ['Yes' if query in vals else 'No' for query in queries]
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

