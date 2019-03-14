#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
        
    n = len(arr)
    m = len(brr)
    
    # first accumulate hashtable of all elements in arr. 
    diff_freq = {}
    for el in arr:
        if el in diff_freq:
            diff_freq[el] += 1
        else:
            diff_freq[el] = 1
    
    k = m-n 
    found_missing = 0
    missing_numbers = set()
    
    # next remove elements as they occur in b. if found 
    # element in b not in a, add to missing_numbers set and
    # increment found_missing by 1, until reach k
    b_ind = 0
        
    #there are k=m-n (non-unique) numbers missing, so if found that many, stop
    while found_missing < k:
        el = brr[b_ind]
        if el in diff_freq: 
            diff_freq[el] -= 1
            #if diff_freq now = 0, remove from hashtable
            if diff_freq[el] == 0:
                diff_freq.pop(el)
        else: #found element in b and not in a
            missing_numbers.add(el)
            found_missing += 1
            
        b_ind += 1
    
    sorted_missing = sorted(list(missing_numbers))
    for el in sorted_missing:
        print(el, end = " ")
        
    return sorted_missing

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

