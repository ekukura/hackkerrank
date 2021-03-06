#!/bin/python3

import math
import os
import random
import re
import sys


def bigSorting(data):
    
    sorted_nums = sorted(unsorted, key = lambda x: (len(x), x))
      
    return sorted_nums


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

