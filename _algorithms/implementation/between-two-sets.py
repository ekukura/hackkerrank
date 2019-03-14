#!/bin/python3

import os
import sys
from math import gcd

#
# Complete the getTotalX function below.
#

def lcm(x,y):
    return int((x*y) / gcd(x,y))

def lcm_list(my_list):
    '''
    note lcm(x1, x2, x3) = lcm(lcm(x1,x2), x3) and in general
    lcm(x_1,...,x_n, a) = lcm(lcm(x1,...,x_n), a)
    '''
    res = my_list[0]
    for i in range(1, len(my_list)):
        res = lcm(res, my_list[i])
    
    return res


def gcd_list(my_list):
    
    res = my_list[0]
    for i in range(1, len(my_list)):
        res = gcd(res, my_list[i])    
        
    return res


def getTotalX(a, b):
    '''
    all numbers x 'between' a and b must have max(a) <= x <= min(b)
    note all numbers which are multiples of all of a are multiples of lcm(a_i)
    and all numbers which are divisors of all of b are divisors of gcd(b_i)
    thus all candidates x have, for some k, j >= 1:
    
        x = k*lcm(a_i) 
        j*x = gcd(b_i)
        
    So then j*k*lcm(a_i) = gcd(b_i)
    
    Thus letting m = gcd(b_i) / lcm(a_i), each distinct factor of m corresponds to a 
    solution, and so the number of factors of m is the answer. If m is not an integer, 
    then there are no solutions.
    
    We can find the number of factors of m by brute force or using m's prime factorization.
    
    '''
    total = 0
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)
    
    if gcd_b % lcm_a == 0: #else, answer is 0
        
        k = int(gcd_b / lcm_a)
        for i in range(1, k + 1):
            if k % i == 0: #then i is a factor
                total += 1
    
    return total

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

