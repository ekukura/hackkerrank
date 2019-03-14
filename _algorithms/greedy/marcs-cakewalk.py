#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    order = calorie.sort(reverse=True)
    min_cals = sum(pow(2,i) * calorie[i] for i in range(len(calorie)))
    return min_cals

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')
    fptr.close()

