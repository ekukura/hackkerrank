#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    n = len(c)
    energy = 100
    cur_cloud = 0
    
    game_over = False
    while not game_over: # jump, calc new energy, check if at start
        
        cur_cloud = (cur_cloud + k) % n
        energy -= (1 + 2 * c[cur_cloud])
        game_over = (cur_cloud == 0)
    
    return energy

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    
    fptr.write(str(result) + '\n')
    fptr.close()

