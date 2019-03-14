#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    
    s = s.replace(" ", "")
    remaining_letters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", 
                         "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                         "S", "T", "U", "V", "W", "X", "Y", "Z"}
    for l in s:
        cur_letter = l.capitalize()
        if cur_letter in remaining_letters:
            remaining_letters -= {cur_letter}
            #print(remaining_letters)
            
    is_pangram = False
    if len(remaining_letters) == 0:
        is_pangram = True
    
    return "pangram" if is_pangram else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

