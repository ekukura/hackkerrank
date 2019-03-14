#!/bin/python3

import os
import sys
import math

# C(n,r) = n!/(n-r)!r! 
# (n-r)!r! = r(r-1)!(n-r+1)!/(n-r+1) = (r/(n-r+1))*(r-1)!(n-(r-1)!) 
# -> C(n,r) = ((n-r+1)/r)*C(n,r-1)

m = int(math.pow(10,9))

# Complete the solve function below.
def solve(n):
    # note C(n,r) = C(n, n-r)
    vals = [1] #vals[r] = C(n,r)
    mid = math.floor(n/2) #e.g. for 5 mid = 2, for 4 mid = 2
    for r in range(1,mid+1):
        next_val = ((n-r+1)*vals[-1]) // r
        vals.append(next_val)  
        
    for r in range(mid+1,n+1):
        next_val = vals[n-r]
        vals.append(next_val)
        
    for val in vals:
        print(val % m, end = " ") 
    
    print("\n", end = "")
    
    return [val % m for val in vals]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

