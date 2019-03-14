# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    cur_item = head
    while (cur_item):
        print(cur_item.data)
        cur_item = cur_item.next
