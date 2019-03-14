#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.

def print_arr(arr):
    
    for el in arr:
        print(el, end = " ")
    print("")
    
def insertSortHelper(arr, insert_ind):
    #at this point, elements in arr at index < insert_ind already sorted 
    insert_val = arr[insert_ind]
    found_insertion_point = False
    cur_ind = insert_ind
    
    while not found_insertion_point:
        if cur_ind == 0:
            arr[cur_ind] = insert_val
            found_insertion_point = True
        else:
            cur_comp_val = arr[cur_ind-1]
            if cur_comp_val < insert_val:
                arr[cur_ind] = insert_val
                found_insertion_point = True
            else:
                arr[cur_ind] = cur_comp_val
                cur_ind -= 1
              
def insertionSort2(n, arr):
    #first position already "sorted"
    if n == 1:
        print(arr)
    else:
        cur_insert_ind = 1
        while cur_insert_ind < n:
            insertSortHelper(arr, cur_insert_ind)
            print_arr(arr)
            cur_insert_ind += 1

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

