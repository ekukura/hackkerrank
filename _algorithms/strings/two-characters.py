#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
import itertools

def remove_chars(s, eliminated_chars): #remove the chars in eliminated_chars from s
    
    new_s = ""
    for c in s:
        if c not in eliminated_chars:
            new_s += c 
            
    return new_s


def remove_consecutive_chars(s):

    char_cands = dict() #char_cands[c] = {last_ind; True/false} if no consec; false otherwise
    for ind in range(1, len(s)):
        c = s[ind]
        if c not in char_cands:
            char_cands[c] = {"last index": ind, "candidate": True}
        else:
            cur_char = char_cands[c]
            if cur_char["candidate"]:
                if cur_char["last index"] == ind-1:
                    cur_char["candidate"] = False
                else:
                    cur_char["last index"] = ind
            
    eliminated_chars = [ch for ch in char_cands if not char_cands[ch]["candidate"]]
    #print(eliminated_chars)
    
    modified_s = remove_chars(s, eliminated_chars)
    return modified_s


def get_max_alternating_len(s, pair): #e.g. try abacab for a,b : 0 for a,c:0, for b,c: 3
    
    x,y = pair
    pair = {x,y}
    #print(pair)
    cur_len = 0
    last_char = ""
    for c in s:
        if c in pair: #otherwise, ignore it
            if c == last_char:
                return 0 #back to back characters
            else:
                cur_len += 1
                last_char = c
                
    return cur_len
                

# Complete the solve function below.
def solve(s):

    #do one pass to determine any chars that occur consecutively and also all
    #chars present
    len1 = len(s)
    modified = True
    while modified:
        s = remove_consecutive_chars(s)
        len2 = len(s)
        if len1 == len2:
            modified = False
        else:
            len1 = len2

    #now in reduced form, can check over all possible combos
    cands = {c for c in s}
    cand_pairs = {pair for pair in itertools.combinations(cands, 2)}
    #take every two pair, record max length

    abs_max = 0
    for pair in cand_pairs:
        cur_max = get_max_alternating_len(s, pair)
        #max_cand_len[pair] = get_max_alternating_len(s, pair) #don't need to keep track of what is for what
        if cur_max > abs_max:
            abs_max = cur_max
    
    print(abs_max)
    return(abs_max)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = solve(s)

    fptr.write(str(result) + '\n')

    fptr.close()

