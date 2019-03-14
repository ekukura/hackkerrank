#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    res = 1
    for val in range(2, n+1):
        res *= val
    print(res)
    
if __name__ == '__main__':
    
    n = int(input())
    extraLongFactorials(n)

