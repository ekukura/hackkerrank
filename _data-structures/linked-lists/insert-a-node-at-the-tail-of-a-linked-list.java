    // Complete the insertNodeAtTail function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {

            SinglyLinkedListNode insertNode = new SinglyLinkedListNode(data);
            SinglyLinkedListNode headNode = null;
                
            if (head == null)
                headNode = insertNode;
            else
            {
                SinglyLinkedListNode curNode = head;
                while (curNode.next != null)
                    curNode = curNode.next;
                
                curNode.next = insertNode;
                headNode = head;
            }
        
        return headNode;

    }
