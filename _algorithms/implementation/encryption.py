#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.

def get_dims(L):
    
    lower_lim = int(math.floor(math.sqrt(L)))
    upper_lim = int(math.ceil(math.sqrt(L)))
    if lower_lim == upper_lim:
        rows = columns = lower_lim
    elif lower_lim * upper_lim >= L:
        rows = lower_lim
        columns = upper_lim #L is not a perfect square, either need rows = lower_lim and cols = upper_lim or both = upper
    else:
        rows = columns = upper_lim
    return rows, columns

def encryption(s):
    
    L = len(s)
    rows, columns = get_dims(L)    
    print(rows, columns)
    
    chars = [c for c in s]
    arr = []
    for row in range(rows-1):
        arr.append([])
        for col in range(columns):
            arr[row].append(chars[row*columns+col])
    #do last, possibly non-full row
    arr.append([])    
    for ind in range((rows-1)*columns, L):
        arr[rows-1].append(chars[ind])
    
    res = ""      
    n_full_cols = len(arr[rows-1])   
    for col in range(n_full_cols):
        for row in range(rows):
            res += arr[row][col]
        res += " "
        
    #do remaining columns (which don't have last row)
    for col in range(n_full_cols, columns):
        for row in range(rows-1):
            res += arr[row][col]
        res += " "     
        
    return res

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

