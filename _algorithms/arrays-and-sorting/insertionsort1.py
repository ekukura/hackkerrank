#!/bin/python3

import math
import os
import random
import re
import sys

def print_arr(arr):
    
    for el in arr:
        print(el, end = " ")
    print("")

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    
    if n == 1:
        print(arr)
    else:
        insert_num = arr[n-1]
        found_insertion_point = False
        cur_ind = n-1
        
        while not found_insertion_point:
            if cur_ind == 0:
                arr[cur_ind] = insert_num
                print_arr(arr)
                found_insertion_point = True
            else:
                cur_comp_val = arr[cur_ind-1]
                if cur_comp_val < insert_num:
                    arr[cur_ind] = insert_num
                    print_arr(arr)
                    found_insertion_point = True
                else:
                    arr[cur_ind] = cur_comp_val
                    print_arr(arr)
                    cur_ind -= 1
                
            

if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

