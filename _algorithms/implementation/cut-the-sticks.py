#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    # build initial dict
    num_sticks = list()
    freq = dict() #store (length, number of sticks) pairs

    for val in arr:
        if val not in freq:
            freq[val] = 1
        else:
            freq[val] += 1;
            
    sticks_queue = [{"value": val, "freq": freq[val]} for val in freq]
    sticks_queue.sort(key=lambda stick: -stick["value"])

    # iterate until dict empty (cut all sticks)
    while sticks_queue:
#         print("STICKS")
#         print(sticks_queue)
        num_sticks.append(sum(stick["freq"] for stick in sticks_queue))
        
        #subtract min val and determining new min val
        shortest = sticks_queue.pop()
        
        for stick in sticks_queue:
            stick["value"] -= shortest["value"]
        
    return num_sticks

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

