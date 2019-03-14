#!/bin/python3

import math
import os
import random
import re
import sys

def pop_next_mountain_or_valley(remaining_stack):
    '''
    :type remaining_stack: list
    :param remaining_stack: contain's only 'U' and 'D' characters
    
    given a remaining_stack of 'U's and 'D', which starts at sea level,
    this pops off the next mountain or valley, and returns 1 if it was 
    a valley and 0 if it was a mountain, or -1 if it was incomplete:
    
    Assumes that remaining_stack is non-empty
    '''
    #print("remaining_stack = \n{}\n".format(remaining_stack))
    
    first_el = remaining_stack.pop()
    cur_stack = [first_el]
    #print("cur_stack = \n{}\n".format(cur_stack))
    
    found_complete_mountain_or_valley = False
    while not found_complete_mountain_or_valley and len(remaining_stack) > 0:
        
        cur_el = remaining_stack.pop()
        
        if cur_el == cur_stack[-1]:
            cur_stack.append(cur_el)
        else:
            cur_stack.pop()
            
        #print("cur_stack = \n{}\n".format(cur_stack))
        if len(cur_stack) == 0:
            found_complete_mountain_or_valley = True

    if not found_complete_mountain_or_valley:
        return -1
    
    else:
        return 1 if first_el == 'D' else 0
    
# Complete the countingValleys function below.
def countingValleys(n, s):
    '''
    :type s: str
    '''
    
    input_stack = list(reversed(list(s)))
    n_valleys = 0
    while len(input_stack) > 0:
        n_valleys += pop_next_mountain_or_valley(input_stack)
        #print("n_valleys = {}\n".format(n_valleys))
        
    return n_valleys
    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()
    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')
    fptr.close()

