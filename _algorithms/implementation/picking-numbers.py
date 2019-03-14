#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
        a.sort()
        combo_max = 2
        first = a[0]
        first_count = 1
        second_count = 0
        for ind in range(1, len(a)):
            el = a[ind]
            if el == first:
                first_count += 1
            elif el == first+1:
                second_count += 1
            else: # reached end of stretch
                cur_combo = first_count + second_count
                if cur_combo > combo_max:
                    combo_max = cur_combo
                    
                if el == first+2 and second_count > 0:                   
                    first = first+1
                    first_count = second_count
                    second_count = 1
                else:
                    first = el
                    first_count = 1
                    second_count = 0
        # last compare last stretch with max
        cur_combo = first_count + second_count
        if cur_combo > combo_max:
            combo_max = cur_combo

        return combo_max
     
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')
    fptr.close()

