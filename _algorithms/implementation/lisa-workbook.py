#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 1
    special_problems = 0
    for chapter in range(n):
        # for current chapter, count number of special problems
        # k problems per page, arr[chapter] problems in chapter
        chapter_problems = arr[chapter]
        cur_problem = 0
        while cur_problem < chapter_problems:
            problems_on_page = min(chapter_problems - cur_problem, k)
            if cur_problem < page and page <= cur_problem + problems_on_page:
                special_problems += 1
            cur_problem += problems_on_page
            page += 1
    return special_problems

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')
    fptr.close()

