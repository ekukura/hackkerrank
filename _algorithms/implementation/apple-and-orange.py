#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    '''
    The num of apples that fall on sam's house is the number 
    of a + x that fall in [s,t] 
    for x in apples, and the num of oranges is b + y that 
    fall in [s,t] for y in oranges
    '''
    apple_count = 0
    orange_count = 0
    
    for apple in apples:
        apple_location = a + apple
        if apple_location >= s and apple_location <= t:
            apple_count += 1
        
    for orange in oranges:
        orange_location = b + orange
        if orange_location >= s and orange_location <= t:
            orange_count += 1
    
    print(apple_count)
    print(orange_count)
    
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

