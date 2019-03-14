# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    
    cur_node = head
    
    while cur_node.next:
        next_node = cur_node.next
        # switch links direction
        cur_node.next = cur_node.prev
        cur_node.prev = next_node
        # move to next node
        cur_node = next_node
    
    # reached end; still need to change pointers at last node
    cur_node.next = cur_node.prev
    cur_node.prev = None
    return cur_node      
    
