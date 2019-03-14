#!/bin/python3

import math
import os
import random
import re
import sys

letters = 'abcdefghijklmnopqrstuvwxyz'
letter_pos = { letters[i]: i for i in range(len(letters)) }

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    
    print(letter_pos)
    max_height = h[letter_pos[word[0]]]
    for ind in range(1, len(word)):
        cur_letter = word[ind]
        cur_height = h[letter_pos[cur_letter]]
        if cur_height > max_height:
            max_height = cur_height
        
    return len(word)*max_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

