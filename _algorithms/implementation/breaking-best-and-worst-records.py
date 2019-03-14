#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    
    max_breaks = 0    
    min_breaks = 0
    
    cur_max = scores[0]
    cur_min = scores[0]

    for game in range(1, len(scores)):
        game_score = scores[game]
        if game_score < cur_min:
            min_breaks += 1
            cur_min = game_score
        elif game_score > cur_max:
            max_breaks += 1
            cur_max = game_score
    
    print(max_breaks, min_breaks)
    return (max_breaks, min_breaks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

