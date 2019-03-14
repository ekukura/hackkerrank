#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck_balance = 0
    # first sum all with importance 0 (T=0)
    luck_balance += sum(contest[0] for contest in contests if contest[1] == 0)
    # then choose the k important contensts (T=1) with maximum luck L to lose
    sorted_important_contest_lucks = sorted([contest[0] for contest in contests if contest[1] == 1], reverse=True)
    luck_balance += sum(sorted_important_contest_lucks[:k])
    # subtract remaining contests luck balance from sum
    luck_balance -= sum(sorted_important_contest_lucks[k:])
    
    return luck_balance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')
    fptr.close()

