

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            cur = self.root
            inserted = False
            while not inserted:
                if new_node.info <= cur.info:
                    # insert left if no left child, else keep going
                    if cur.left:
                        cur = cur.left
                    else:
                        # insert
                        cur.left = new_node
                        inserted = True
                else:
                    # insert right if no right child, else keep going
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = new_node
                        inserted = True
                    


