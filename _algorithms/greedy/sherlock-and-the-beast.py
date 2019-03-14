#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
        
    impossible_lengths = {0,1,2,4,7}
    if n in impossible_lengths:
        print(-1)
    
    else:
        # divide by 3. try with this divisor, then decrease by 1 until get something
        # divisible by 5
        d3 = int(math.floor(n/3))
        d5 = None
        r = None
        # n = 3*d3 + r. Is r divisible by 5?
        
        found_combo = False
        # each iteration, when decrease d3 by 1, increase r by 3, so must find
        # an r divisible by 5 within 5 iterations
        while not found_combo and d3 >= 0: # don't really need d3 >= 5 condition, but it makes it safe
            r = n - 3*d3
            if r % 5 == 0:
                d5 = int(r/5)
                found_combo = True
                # n = 3*d3 + r = 3*d3 + 5*d5
            else:
                d3 -= 1
           
        res_str = '5' * 3*d3 + '3' * 5*d5
        print(res_str)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

