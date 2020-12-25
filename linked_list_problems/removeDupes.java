package linked_list_problems;

import java.util.*;
/*
 * Cracking the Coding Interview 2.1: Write code to remove duplicates from an
 * unsorted linked list.
 * 
 * What does unsorted mean in this case? Can we make any assumptions about the
 * kinds of data stored in the linked list?
 * 
 * Does it matter which instance of the duplicate is deleted? go with the second
 * 
 * Do we have a singly linked, or doubly linked? SLL
 * 
 * Assume that there's only integer elements, and anywhere from 0-> n nodes.
 * 
 * Test input: 
 *                    p     n 
 * 1 --> -1 --> 6 --> 5  --> 7 --> 
 *                    p     
 * node = target = Node(1)
 * 
 * removing == "deleting"? yes
 * 
 * // two approaches:
 *  1. move the target node by moving the prev.next pointer
 *  2. move the node up to the new node ahead of previous
 *  3. while loop for deleting nodes
 * 
 * Deletion on a small input 1 --> 2 --> 3 --> 1 --> 3 -->
 * 
 * Test output: 
 * 1 --> -1 --> 6 --> 5 --> 7 -->
 * {1, -1, 6, 5, 7}
 * 
 * # intution: keep a "memory" of what keys have been seen before
 * # approach: 
 * use a HashSet
 * iterate over the LL
 *      if seen before: do a deletion
 *      else: add it to the HashSet (for use when checking)
 * return value? the ll
 * 
 * # edge case: empty LinkedList? --> return null
 */

 class LinkedList {
    /* Node class declaration */
    class Node {
        int data;
        Node next;

        public Node(int d) {
            this.data = d;
            this.next = null;
        }
        
    }
    // Linked List instance variables
    public Node head;

    public LinkedList() {
        this.head = null;
    }

    public void delete(Node prev, Node target) {
        // remove the node targeted for deletion from the list
        prev.next = target.next;
        // move the pointer at the deleted node up to the new successor
        target = prev.next;
    }

    public LinkedList removeDuplicates() {
        // use a HashSet
        HashSet<Integer> uniqueElements = new HashSet<Integer>();
        // iterate over the LL with 2 pointers
        Node prev = null, n = this.head;
        while (n != null) {
            // if prev or node seen before: 
            if (uniqueElements.contains(n.data) == true) {
                // do a deletion
                this.delete(prev, n);
            } else {
                // otherwise add it to the HashSet
                uniqueElements.add(n.data);
                // move the pointers ahead
                prev = n;
                n = n.next;
            }
        }   
        // return the results
        return this;
    }

    public static void main(String[] main) {
        int[] items = {1, -1, 6, 5, 1, 5, 7};
        // make Nodes for each item
        LinkedList ll = new LinkedList();
        ll.head = ll.new Node(items[0]);
    }
 }