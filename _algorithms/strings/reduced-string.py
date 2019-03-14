#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the super_reduced_string function below.
def super_reduced_string(s):
    
    cur_index = 0
    print(len(s))
    while cur_index < len(s) - 1: #if at last character, stop 
        if s[cur_index] == s[cur_index+1]:
            s = s[0:cur_index] + s[cur_index + 2:]
            cur_index = 0 #start at beginning again to check for new things
        else:
            cur_index += 1
    
    if len(s) == 0:
        return "Empty String"
    else:
        return s
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = super_reduced_string(s)

    fptr.write(result + '\n')

    fptr.close()

