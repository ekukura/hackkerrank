#!/bin/python3

import os
import sys

def stacks_equal(the_stacks):
    
    height1 = the_stacks[0]["height"]
    height2 = the_stacks[1]["height"]
    height3 = the_stacks[2]["height"]
    
    if height1 == height2 and height2 == height3:
        return True
    else:
        return False
#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    # First reverse the stacks, as the pop() method will currently remove from back not front
    h1.reverse()
    h2.reverse()
    h3.reverse()
    # remove a cylinder from the highest stack until all stacks have equal height
    stacks = [{"stack": h1, "height": sum(h1)},
           {"stack": h2, "height": sum(h2)},
           {"stack": h3, "height": sum(h3)}
           ]
    
    #check for equality. If equal print height.
    while not stacks_equal(stacks):
        # get tallest stack
        tallest_stack = max(stacks, key = lambda s: s["height"])
        # pop tallest element off
        removed_height = tallest_stack['stack'].pop()
        tallest_stack['height'] -= removed_height
    
    max_equal_height = stacks[0]['height']
    print(max_equal_height)
    return max_equal_height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

