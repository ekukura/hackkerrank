#!/bin/python3

import math
import os
import random
import re
import sys
import copy

def is_palindrome(s):
    # always compare s[0:floor(n/2)] to s[ceil(n/2):]
    first = s[:math.floor(len(s)/2)]
    second = s[math.ceil(len(s)/2):][::-1]
    return first == second

def trim(s):
    # trims mirrored ends off strings
    found_mismatch = False
    i = 0
    while not found_mismatch and len(s) > 1:
        if s[0] == s[-1]:
            s = s[1:-1]
            i += 1
        else:
            found_mismatch = True
    
    return s, i
    
# Complete the palindromeIndex function below.
def palindromeIndex(s):
    
    r, ind = trim(s) # ind is # chars chopped off either end
    # after trimming, if can remove one letter off either end and get a palindrome, good
    
    # first check if s is a palindrome
    if len(r) <= 1:
        return -1
    else:
        # check if possible to remove one letter to make 
        # naive approach: just modify string, try removing one letter at a time
        left = r[1:]
        if is_palindrome(left):
            return ind
        right = r[:-1]
        if is_palindrome(right): #abcdba'
            return len(s) - ind - 1
        
        else:
            return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')

    fptr.close()

