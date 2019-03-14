# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    
    node = SinglyLinkedListNode(data)
    
    if position == 0:
        node.next = head
        head = node
    
    else:
        # if not inserting at head, loop until the next node at the insert position
        cur_node = head
        next_node_pos = 1
        while next_node_pos < position:
            cur_node = cur_node.next
            next_node_pos += 1

        # once reach here, next_node_pos = position, so insert after the cur_node
        node.next = cur_node.next
        cur_node.next = node
        
    return head
    
    
