# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    
    cur_node = head
    while cur_node:  
        found_next_unique_node = False
        next_node = cur_node.next
        while (not found_next_unique_node):
            if next_node:
                if cur_node.data == next_node.data:
                    next_node = next_node.next
                else:
                    found_next_unique_node = True
                    cur_node.next = next_node
                    cur_node = next_node # move to unique node
            else:
                found_next_unique_node = True
                cur_node.next = None
                cur_node = None
                
    return head
    
