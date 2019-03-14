#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    cycle_number = math.ceil(math.log2(t/3 + 1))
    # now find out what r is
    smallest_in_cycle = 3*(pow(2, cycle_number-1) - 1) + 1
    index_in_cycle = t - smallest_in_cycle
    # start at value 3 * (2 ^ (k-1))
    start_value = 3*(pow(2, cycle_number-1))
    return start_value - index_in_cycle

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    result = strangeCounter(t)

    fptr.write(str(result) + '\n')
    fptr.close()

