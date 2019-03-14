#!/bin/python3

import math
import os
import random
import re
import sys

def letters_changed(sos_string):
    '''
    :type sos_string: str
    :param sos_string: some 3-letter string
    :return number of character difference from the string 'SOS'
    '''
    #print('sos_string: {}\n'.format(sos_string))
    sos = ['S','O','S']
    sos_returned = list(sos_string)
    
    num_changed_chars = sum([1 for i in range(3) if sos[i] != sos_returned[i] ])
    return num_changed_chars

# Complete the marsExploration function below.
def marsExploration(s):
    
    n_changed_chars = 0
    n_sos_calls = int(len(s)/3)
    for call in range(n_sos_calls):
        n_changed_chars += letters_changed(s[3*call:3*call+3])

    return n_changed_chars
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

