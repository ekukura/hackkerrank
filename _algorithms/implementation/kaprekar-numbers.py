#!/bin/python3

import math
import os
import random
import re
import sys

def is_kap(n):
    d = len(str(n))
    square = pow(n,2)
    string_n2 = str(square)
    l = int(string_n2[:-d]) if len(string_n2) > 1 else 0
    r = int(string_n2[-d:])
    return l + r == n

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    numbers = [str(n) for n in range(p, q+1) if is_kap(n)]
    if not numbers:
        print("INVALID RANGE")
    else:
        print(" ".join(numbers))

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)

