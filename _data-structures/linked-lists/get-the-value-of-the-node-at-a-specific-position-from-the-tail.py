# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    
    list_arr = []
    cur_node = head
    
    # traverse linked list, putting in array as go.
    while cur_node:
        list_arr.append(cur_node.data)
        cur_node = cur_node.next
            
    # once reached end of list, pull out correct node
    return list_arr[-(positionFromTail+1)]

