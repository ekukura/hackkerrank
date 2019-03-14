#!/bin/python3

import math
import os
import random
import re
import sys

def match(right_bracket, left_bracket):
    
    match = False
    if right_bracket == ")":
        if left_bracket == "(":
            match = True
    elif right_bracket == "}":
        if left_bracket == "{":
            match = True
    elif right_bracket == "]":
        if left_bracket == "[":
            match = True

    return match

# Complete the isBalanced function below.
def isBalanced(s):
    '''
    
    :param s:
    :type s: str
    '''
    brackets = [c for c in s]
    
    n = len(brackets)
    left_brackets = []
    cur_idx = 0
    
    matched = True
    while matched and cur_idx < n:
        next_char = brackets[cur_idx]
        if  next_char in {"{", "[", "("}:
            left_brackets.append(next_char)
            cur_idx += 1
        else: #next_char in {"}", "]", ")"}:
            #right bracket -- needs to match top element in left_brackets
            if len(left_brackets) == 0:
                matched = False
            else:
                top_left = left_brackets[-1]
                if match(next_char,top_left):
                    left_brackets.pop()
                    cur_idx += 1
                else:
                    matched = False
                
    if not matched or len(left_brackets) > 0:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

