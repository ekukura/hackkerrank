#!/bin/python3

def print_arr(arr):
    for el in arr:
        print(el, end = " ")

def left_rotation(arr, d):
    #since d lr's performed, first element of new arr should be at position d,
    #and first d elements should be appended at end of array
    new_arr = arr[d:]
    new_arr.extend(arr[0:d])
    print_arr(new_arr)

if __name__ == '__main__':
   
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    left_rotation(a, d)

