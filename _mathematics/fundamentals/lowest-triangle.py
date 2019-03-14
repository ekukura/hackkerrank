#!/bin/python3

import math

def lowestTriangle(base, area):
    # Complete this function
    #base*height/2 = area, so exact height to give area is 2*area/base
    non_int_height = 2*area/base
    return int(math.ceil(non_int_height))

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
