

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    #Enter your code here
    smaller = min(v1, v2)
    larger = max(v1, v2)
    if smaller <= root.info and larger >= root.info:
        # this means root is the lca since they are on different
        # sides of the tree
        return root
    elif larger < root.info:
        # both on left side, call recursively on left child
        return lca(root.left, v1, v2)
    else: # smaller > root.info
        return lca(root.right, v1, v2)




