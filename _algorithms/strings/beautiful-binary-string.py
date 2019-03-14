#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    """
    :type b: str 
    e.g. "01010" 
         "11010"
    """
    num_changed = 0
    n = len(b)
    start_ind = 0

    while start_ind < n-2: 
        # 3-bit possibilities: 000, 001, 010, 011, 100, 101, 110, 111
        first_bit = b[start_ind]
        if first_bit == '1': #move on, nothing bad can start with this
            start_ind += 1
        else: #first_bit=0 # possiblities: 000, 001, 010, 011
            second_and_third_bit = b[start_ind + 1: start_ind + 3]
            if second_and_third_bit == '10': #010 -> increment num_changed and move to next triplet
                num_changed += 1
                start_ind += 3
            elif second_and_third_bit == '11': #011 -> move to next triplet
                start_ind += 3
            # below two could be optimized -- already done some of the work
            elif second_and_third_bit == '00': #000 -> move start index up + 2
                start_ind += 2
            else: #001 -> move start index + 1
                start_ind += 1        
    
    return num_changed

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    b = input()
    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')
    fptr.close()

