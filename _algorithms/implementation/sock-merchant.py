#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    num_pairs = 0
    unmatched_socks = dict() #contains only 0's and 1's
    for sock in range(n):
        color = ar[sock]
        if color in unmatched_socks and unmatched_socks[color] == 1: #match, increment num_pairs, then put back at 0
            num_pairs += 1
            unmatched_socks[color] = 0
        else: #unmatched_socks[color] = 0 or color not in unmatch_socks
            unmatched_socks[color] = 1
            
    print(num_pairs)
    return(num_pairs)
    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()

