#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    n_lines = len(grid)
    # don't need to look at first or last line
    for row in range(1, n_lines-1):
        # don't need to look at first or last col
        last_cell_cavity = False
        for col in range(1, n_lines-1):
            # if last cell WAS a cavity, means current cell shallower then its left neighbor, so it ISN'T
            if not last_cell_cavity:
                # check if current cell is a cavity
                cur_val = grid[row][col]
                largest_adj = max(grid[row][col-1], grid[row][col+1], grid[row-1][col], grid[row+1][col])
                if largest_adj < cur_val:
                    # is a cavity
                    grid[row] = grid[row][:col] + 'X' + grid[row][col+1:]
                    last_cell_cavity = True
            else:
                last_cell_cavity = False
                
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

