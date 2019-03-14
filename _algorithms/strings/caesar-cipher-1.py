#!/bin/python3

import math
import os
import random
import re
import sys

import re

encrypted_regex = re.compile("[A-Za-z]")

def create_encryption_map(shift):
    mapping = {}
    letters = "abcdefghijklmnopqrstuvwxyz"
    n = len(letters)
    shift = shift % n
    for i in range(n - shift):
        cur_letter = letters[i]
        enc_letter = letters[i+shift]
        mapping[cur_letter] = enc_letter
        mapping[cur_letter.capitalize()] = enc_letter.capitalize()
         
    for i in range(shift):
        cur_letter = letters[n - shift + i]
        enc_letter = letters[i]
        mapping[cur_letter] = enc_letter
        mapping[cur_letter.capitalize()] = enc_letter.capitalize()
        
    return mapping

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    
    encryption_map = create_encryption_map(k)
    encrypted_string = ""
    
    for l in s:
        if re.match(encrypted_regex, l): 
            encrypted_string += encryption_map[l]
        else:
            encrypted_string += l
        
    return encrypted_string

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')
    fptr.close()

