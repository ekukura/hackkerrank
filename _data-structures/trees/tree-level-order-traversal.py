"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def printLevel(root, level):
    # return true if printed anything on this level, else false
    # indicating to stop
    level_empty = False
    if root:
        if level == 0:
            print(root.info, end=' ')
        else:
            left_empty = printLevel(root.left, level-1)
            right_empty = printLevel(root.right, level-1)
            if left_empty and right_empty:
                level_empty = True
    else:
        level_empty = True
    
    return level_empty
    
def levelOrder(root):
    #Write your code here
    cur_level = 0
    level_empty = False
    while not level_empty:
        level_empty = printLevel(root, cur_level)
        cur_level += 1
