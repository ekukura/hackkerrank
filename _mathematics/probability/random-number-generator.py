#!/bin/python3

import os
import sys
from fractions import Fraction

# Complete the solve function below.
def solve(a, b, c):
    s = min(a,b)
    l = max(a,b)
    
    if l <= c:
        if c - l > s: # then s + l = a + b < c
            num = 1
            den = 1
        else: # c-l <= s
            # 3 pieces
            # 1 * (c-l)
            # (s - (c-l))*(c-s)/l
            # (s - (c-l))*(1-(c-s)/l)/2
            num = 2*c*(l+s) - (int(pow(s,2))+int(pow(c,2))+int(pow(l,2)))
            den = 2*l*s         
    elif s <= c and c <= l:
        num = s*(2*c-s)
        den = 2*l*s
    else: # c <= s
        # (c/l) * c / 2 = c^2/(2*l)
        num = int(pow(c,2))
        den = 2*l*s
        
    res = Fraction(num, den)
    return "{}/{}".format(res.numerator, res.denominator)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        abc = input().split()
        a = int(abc[0])
        b = int(abc[1])
        c = int(abc[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()

