#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    sorted_stations = sorted(c)
    first_endpoint_dist = sorted_stations[0]
    last_endpoint_dist = n-sorted_stations[-1]-1
    max_end_dist = max(first_endpoint_dist, last_endpoint_dist)
    if len(sorted_stations) > 1:
        middle_distances = [sorted_stations[i]-sorted_stations[i-1] for i in range(1,len(sorted_stations))]
        longest_mid = math.floor(max(middle_distances)/2)
        max_dist = max(longest_mid, max_end_dist)
    else:
        max_dist = max_end_dist
    
    return max_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')
    fptr.close()

