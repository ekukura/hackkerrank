#!/bin/python3

import math
import os
import random
import re
import sys

def count_chars(s):
    s_count = dict()
    
    for c in s:
        s_count[c] = s_count.get(c, 0) + 1
    
    return s_count

def makingAnagrams(s1, s2):
    s1_counts = count_chars(s1)
    s2_counts = count_chars(s2)
    
    # count common characters
    common = 0
    common_chars = set.intersection(set(s1_counts.keys()), set(s2_counts.keys()))
    for c in common_chars:
        common += min(s1_counts[c], s2_counts[c])
    
    ns1_chars = sum(s1_counts.values())
    ns2_chars = sum(s2_counts.values())
    
    # num deletions = (total count in s1 - common) + (count in s2 - common)
    ndel = (ns1_chars - common) + (ns2_chars - common)
    return ndel

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')
    fptr.close()

