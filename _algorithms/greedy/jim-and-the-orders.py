#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    customer_orders = [[i+1, orders[i][0] + orders[i][1]] for i in range(len(orders))]
    sorted_ords = sorted(customer_orders, key=lambda c: (c[1],c[0]))
    jim_orders = [item[0] for item in sorted_ords]
    return jim_orders

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

