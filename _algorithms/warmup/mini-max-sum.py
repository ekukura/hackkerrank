#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    total_sum = sum(arr)
    min_num = min(arr)
    max_num = max(arr)
    
    min_sum = total_sum - max_num
    max_sum = total_sum - min_num
    
    print(str(min_sum) + " " + str(max_sum))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

