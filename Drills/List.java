import java.util.ArrayList;

class LinkedList {
    // ListNode class definition
    class ListNode {
        int key;
        ListNode next;

        public ListNode(int key) {
            this.key = key;
            this.next = null;
        }

        public int getKey() {
            return this.key;
        }

        public void setKey(int newKey) {
            this.key = newKey;
            return; 
        }

        public ListNode getNext() {
            return this.next;
        }

        public void setNext(ListNode newNext) {
            this.next = newNext;
            return;
        }
    }

    // LinkedList class definition
    ListNode head;

    public LinkedList(ListNode head) {
        this.head = head;
    }

    // get all the items in the linked list
    public int[] getAllIterative() {
        ListNode curNode = this.head;
        // get all the items in an ArrayList
        ArrayList<Integer> items = new ArrayList<Integer>();
        while (curNode != null) {
            items.add(curNode.key);
            curNode = curNode.next;
        }
        // init the array and its index
        int[] values = new int[items.size()];
        // put all the items in an array
        int index = 0;
        for(Integer item:items) {
            values[index] = item;
            index = index + 1;
        }
        // return the array
        return values;
    }

    public int[] getAllRecursive() {
        // init an array list
        ArrayList<Integer> items = new ArrayList<Integer>();
        // populate the arrayList
        ListNode curNode = this.head;
        return this.getAllRecursive(items, curNode);
    }

    public int[] getAllRecursive(ArrayList<Integer> items, ListNode curNode) {
        // Base Case: the ArrayList has all the keys
        if (curNode == null) {
            // make a new static array
            int[] values = new int[items.size()];
            // place all items in the array
            int index = 0;
            for (Integer item:items) {
                values[index] = item;
                index += 1;
            }
            // return the array
            return values;
        // Recursive Case: add the next item to the ArrayList
        } else {
            // add to the ArrayList from the current list node
            items.add(curNode.getKey());
            // update the current list node
            curNode = curNode.getNext();
            // on to the next stack frame!
            return this.getAllRecursive(items, curNode);
        }
    }

    // prepend to the list
    public void prepend(int newValue) {
        // make a new ListNode
        ListNode newHead = new ListNode(newValue);
        // make it precede the current head
        newHead.setNext(this.head);
        // make it the new head
        this.head = newHead;
        return;
    }

    // append to the list
    public void append(int newValue) {
        // make a new node
        ListNode newTail = new ListNode(newValue);
        // place it after the last Node
        ListNode curNode = this.head;
        while (curNode.next != null) {
            curNode = curNode.next;
        }
        curNode.setNext(newTail);
        return;
    }

    // delete from the linked list
    public void delete(int deleteKey) {
        // traverse the list using two nodes
        ListNode prev = null, curNode = this.head;

        // find the deleteKey
        while (curNode.key != deleteKey) {
            // if not found yet, keep moving
            prev = curNode;
            curNode = curNode.next;
        }

        // if prev and curNode not None, update it's previous
        if (prev != null && curNode != null) {
            prev.next = curNode.next;
        }
        // if the head is being deleted, then update the head
        else if (this.head.key == deleteKey) {
            this.head = this.head.next;
        }
        return; 
    }
}