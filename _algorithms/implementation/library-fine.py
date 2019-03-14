#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    """
    d1.m1.y1 for returned date
    d2.m2.y2 for due date
    
    (1) Book returned on or before due date
        - fine = 0
    (2) Book late, later day; same month and year
        - fine = 15 * days late
    (3) Book late, later month; same year
        - fine = 500 * num months
    (4) Book late, later year
        - fine = 10,000
    """
    if y1 > y2: #case 4
        return 10000
    
    elif y1 == y2:
        
        if m1 > m2: # case 3
            return 500 * (m1 - m2)
        
        elif m1 == m2:
            
            if d1 > d2: # case 2
                return 15 * (d1 - d2)
            else: # d1 <= d2; m1,y1 = m2,y2
                return 0
        
        else: # m1 < m2 ; y1 = y2 -- case 1
            return 0
        
    else: #y1 < y2 -- case 1
        return 0
        
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')
    fptr.close()

