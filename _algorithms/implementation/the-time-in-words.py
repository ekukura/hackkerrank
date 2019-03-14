#!/bin/python3

import math
import os
import random
import re
import sys

ones_map = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
teen_map = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "forteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

# Complete the timeInWords function below.
def timeInWords(h, m):

    if m <= 30: # use past
        word_hour = ones_map[h] if h < 10 else teen_map[h]
    else: # use to
        if h == 12:
            word_hour = "one"
        else:
            word_hour = ones_map[h+1] if h < 9 else teen_map[h+1]

    if m == 0:
        return "{} o' clock".format(word_hour)
    elif m == 1:
        return "one minute past {}".format(word_hour)
    elif m < 15: # 2 <= m <= 14
        word_min = ones_map[m] if m < 10 else teen_map[m]
        return "{} minutes past {}".format(word_min, word_hour)
    elif m == 15:
        return "quarter past {}".format(word_hour)
    elif m < 30: # 16 <= m <= 29
        word_min = teen_map[m] if m < 20 else "twenty "+ones_map[m%10] 
        return "{} minutes past {}".format(word_min, word_hour)
    elif m == 30:
        return "half past {}".format(word_hour)
    elif m < 45: # 31 <= m <= 44
        word_min = teen_map[60-m] if m > 40 else "twenty "+ones_map[(60-m)%10] 
        return "{} minutes to {}".format(word_min, word_hour)
    elif m == 45:
        return "quarter to {}".format(word_hour)
    else: # 46 <= m <= 59
        if m == 59:
            return "one minute to {}".format(word_hour)
        else:
            word_min = ones_map[60-m] if m > 50 else teen_map[60-m]
            return "{} minutes to {}".format(word_min, word_hour)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())
    m = int(input())
    result = timeInWords(h, m)

    fptr.write(result + '\n')
    fptr.close()

