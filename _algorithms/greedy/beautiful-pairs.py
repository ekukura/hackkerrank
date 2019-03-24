#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    # Store all beautiful pairs, as long as haven't been seen before
    n = len(A)
    seen_pairs = set()

    seen_as_part_of_pairs = {
        'A': set(),
        'B': set()
    }
    # could also remove i,j pair once seen once
    for i in range(n):
        for j in range(n):
            a = A[i]
            b = B[j]
            if a == b:
                if i in seen_as_part_of_pairs['A']:
                    pass
                elif j in seen_as_part_of_pairs['B']:
                    pass
                else:
                    seen_pairs.add((i, j))
                    # could also just continue to next
                    # i once found a pair
                    seen_as_part_of_pairs['A'].add(i)
                    seen_as_part_of_pairs['B'].add(j)

    num_disjoint_pairs = len(seen_pairs)
    # if have less than n pairs, something is unmatched in A,B and can
    # change one element of B to match the unmatched in A
    if num_disjoint_pairs < n:
        num_disjoint_pairs += 1
    else:
        num_disjoint_pairs -= 1

    return num_disjoint_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')
    fptr.close()

