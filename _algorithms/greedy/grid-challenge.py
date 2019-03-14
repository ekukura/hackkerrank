#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    n = len(grid)
    nc = len(grid[0]) # shouldn't actually need this, problem statement SAYS its square array
    sorted_char_grid = list()
    for row in grid:
        cur_row_chars = [ c for c in row]
        sorted_char_grid.append(sorted(cur_row_chars))
    
    found_unsorted = False
    #print(sorted_char_grid)
    col_ind = 0
    while not found_unsorted and col_ind < nc:
        row_ind = 0
        el = sorted_char_grid[row_ind][col_ind]
        while row_ind < n - 1:
            el2 = sorted_char_grid[row_ind+1][col_ind]
            if el <= el2:
                row_ind += 1
                el = el2
            else:
                found_unsorted = True
                break 
        col_ind += 1     
    
    res = "NO" if found_unsorted else "YES" 
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

