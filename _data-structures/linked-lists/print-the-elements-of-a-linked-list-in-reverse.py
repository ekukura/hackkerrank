# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    
    if not head:
        pass
    
    else:
        next_node = head.next
        if next_node:
            reversePrint(next_node)
        
        print(head.data)
        
            
