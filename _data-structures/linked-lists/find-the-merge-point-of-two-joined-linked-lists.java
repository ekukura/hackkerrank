    // Complete the findMergeNode function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static int findMergeNode(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
        
        SinglyLinkedListNode cur1 = head1;
        int merge_data = -1;
        boolean found_merge_point = false;       
        List<SinglyLinkedListNode> observed = new ArrayList<>();
        
        // find the tail of the first link and append head of second
        while (cur1.next != null)
        {
                cur1 = cur1.next;
        }
        cur1.next = head2;
            
        // look for loop
        SinglyLinkedListNode cur = head1;
        
        while (!found_merge_point)
        {
                if (observed.contains(cur))
            {
                merge_data = cur.data;
                found_merge_point = true;
            }
                else
                {
                    observed.add(cur);
                    cur = cur.next;
                }
        }
        return merge_data;
    }

