#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    cost = 0
    # middle element must be 5
    if s[1][1] != 5:
        cost = abs(5-s[1][1])

    # outside must follow order (starting at a corner)
    # and up to reversal/rotation
    # correct = [6,7,2,9,4,3,8,1]
    outside = [s[0][i] for i in range(3)]
    outside.append(s[1][2])
    outside.extend([s[2][i] for i in range(2,-1,-1)])
    outside.append(s[1][0])

    # there are 8 possible permutations of 'correct'
    # rotate correct by two positions, and for each of these reverse
    
    # also reverse each
    possible_correct = [
        [6, 7, 2, 9, 4, 3, 8, 1],
        [2, 9, 4, 3, 8, 1, 6, 7],
        [4, 3, 8, 1, 6, 7, 2, 9],
        [8, 1, 6, 7, 2, 9, 4, 3],
        [6, 1, 8, 3, 4, 9, 2, 7],
        [2, 7, 6, 1, 8, 3, 4, 9],
        [4, 9, 2, 7, 6, 1, 8, 3],
        [8, 3, 4, 9, 2, 7, 6, 1]
    ]

    # compare each possible correct with outside, and take min cost
    outside_cost = 10000 # something impossible
    for possibility in possible_correct:
        diffs = [abs(outside[i] - possibility[i]) for i in range(8)]
        current_cost = sum(diffs)
        if current_cost < outside_cost:
            outside_cost = current_cost

    cost += outside_cost
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')
    fptr.close()

