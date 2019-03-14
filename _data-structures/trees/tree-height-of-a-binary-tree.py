# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           
       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    
    if not (root.left or root.right):
        return 0
    elif root.left and not root.right:
        return height(root.left) + 1
    elif root.right and not root.left:
        return height(root.right) + 1
    else:
        return max(height(root.left), height(root.right)) + 1
    
