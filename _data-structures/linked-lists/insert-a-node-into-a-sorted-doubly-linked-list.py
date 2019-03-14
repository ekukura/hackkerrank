

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if not head:
        return new_node
    else:
        # check if goes before head; if so insert and return
        if new_node.data <= head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        # find insertion point
        else:
            cur_node = head
            inserted = False
            # insert
            while cur_node and not inserted:
                # know new_node.data > cur_node.data since got here
                if cur_node.next:
                    if new_node.data <= cur_node.next.data:
                        # insertion point
                        # cur_node -> new_node -> cur_node.next
                        new_node.prev = cur_node
                        new_node.next = cur_node.next
                        cur_node.next.prev = new_node
                        cur_node.next = new_node
                        inserted = True
                # if not cur_node.next, at end; insert here
                else:
                    cur_node.next = new_node
                    inserted = True
                    
                cur_node = cur_node.next

            return head



