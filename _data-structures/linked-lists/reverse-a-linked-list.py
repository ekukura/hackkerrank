# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    
    if not head:
        pass
    else:
        next_node = head.next
        if next_node:
            new_head = reverse(next_node)
            next_node.next = head
            head.next = None
        else: #reached end of list
            new_head = head
            
    return new_head
        

