# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    
    if position == 0:
        head = head.next
    else:
        cur_node = head
        cur_pos = 0
        #loop until find node to delete
        while cur_pos + 1 < position: 
            cur_node = cur_node.next
            cur_pos += 1
        #here cur_pos + 1 = position and we want to delete the next node
        node_to_delete = cur_node.next #want to delete this node
        cur_node.next = node_to_delete.next
    
    return head
    
    
