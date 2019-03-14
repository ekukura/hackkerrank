# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    # initialize -- get head of merged list and front node of other list
    if head1.data <= head2.data:
        head = head1
        other_front = head2
    else:
        head = head2
        other_front = head1
        
    cur_merged_node = head
    
    # move along list, comparent current nodes of both lists.
    reached_end = False
    while not reached_end:
        if not cur_merged_node.next:
            cur_merged_node.next = other_front
            reached_end = True
        elif not other_front:
            reached_end = True
        else: #decide
            next_node = cur_merged_node.next
            if  next_node.data <= other_front.data:
                cur_merged_node = next_node
            else:
                cur_merged_node.next = other_front
                cur_merged_node = other_front
                other_front = next_node
        
    return head
            
    
    
