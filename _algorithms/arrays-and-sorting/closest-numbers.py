 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):

    res = list()
    n = len(arr)

    arr.sort()
    # all #'s between -10^7 and 10^7
    min_diff = 2*int(pow(10,7))

    for lower in range(n-1):
        cur_diff = arr[lower+1]-arr[lower]
        if cur_diff == min_diff:
            res.extend([arr[lower], arr[lower+1]])
        elif cur_diff < min_diff:
            res = [arr[lower], arr[lower+1]]
            min_diff = cur_diff

    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

