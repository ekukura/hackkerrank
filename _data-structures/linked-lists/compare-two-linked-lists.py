# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reached_end(node1, node2):
    if not node1 or not node2:
        return True
    else:
        return False

def compare_lists(llist1, llist2):
    #while not at end of list
    det_unequal = False
    cur_l1_node = llist1
    cur_l2_node = llist2
    while (not reached_end(cur_l1_node, cur_l2_node)) and (not det_unequal):
        #compare elements of current level. If equal continue, else return 0
        if cur_l1_node.data == cur_l2_node.data:
            cur_l1_node = cur_l1_node.next
            cur_l2_node = cur_l2_node.next
        else: 
            det_unequal = True
        
    if det_unequal:
        return 0   
    #once at end of one list, check if at end of other. If so then equal
    else:
        if not cur_l1_node and not cur_l2_node:
            return 1
        else:
            return 0
    
    
        
