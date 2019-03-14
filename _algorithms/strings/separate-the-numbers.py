#!/bin/python3

import math
import os
import random
import re
import sys

def sep_numbers_k_len(s, k):
    # if successful, return the first integer of the sequence
    # else return False
    # k is the length of the first integer
    
    int_len = k
    determined_not_beautiful = False
    first_int = int(s[:int_len])
    
    if k > 1:
        if int(s[0]) == 0:
            return False
    
    cur = first_int
    rem = s[int_len:]
    while len(rem) > 0 and not determined_not_beautiful:
        # check if cur is 1 less than a power of 10
        # max length of s is 32 so could only have one change in length (from k to k+1)
        if cur == pow(10,int_len) - 1:
            int_len += 1
        
        if len(rem) < int_len:
            determined_not_beautiful = True
            
        next_int = int(rem[:int_len])
        if next_int == cur+1:
            cur = next_int
            rem = rem[int_len:]
        else:
            determined_not_beautiful = True
            
    if determined_not_beautiful:
        return False
    else:
        return first_int

# Complete the separateNumbers function below.
def separateNumbers(s):
    n = len(s) 
    # means max successful series would have first int len <= floor(n/2)
    cur_start_len = 1
    max_start_len = int(math.floor(n/2))
    beautiful_sequence_found = False
    while not beautiful_sequence_found and cur_start_len <= max_start_len:
        res = sep_numbers_k_len(s, cur_start_len)
        if res:
            beautiful_sequence_found = True
            print("YES {}".format(res))
        else:
            cur_start_len += 1
        
    if not beautiful_sequence_found:
        print("NO")
    
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

