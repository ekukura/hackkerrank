#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    
    total = sum(bill)
    sharable_portion = total - bill[k]
    anna_total = int(sharable_portion/2)
    
    if anna_total == b:
        print("Bon Appetit")
    else:
        print(b-anna_total)
        
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

