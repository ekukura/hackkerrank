#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    money_left = s
    games_bought = 0
    cur_price = p
    
    # while you have enough money to buy another game
    while money_left >= cur_price:
        games_bought += 1
        money_left -= cur_price
        if cur_price - d > m:
            cur_price -= d
        else:
            cur_price = m
    
    return games_bought
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()

