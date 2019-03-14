"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    #Write your code here
    # if null, return immediately
    if root:
        inOrder(root.left)      # print left
        print(root, end = " ")  # print root
        inOrder(root.right)     # print right
    
