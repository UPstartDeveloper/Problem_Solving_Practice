/* 
 * Implement a MyQueue class which implements a queue using two stacks.
 */


public class Node {
    public int val; 
    public Node next;

    public Node(int value) {
        this.val = value;
        this.next = null;
    }
}


public class MyQueue {
    public Node top, bottom;

    public MyQueue(Node topNode){
        this.top = topNode;
        this.bottom = null;
    }

    public int front() {
        int value = null;
        if (this.top != null) {
            value = this.top.val;
        }
        return value;
    }

    public void enqueue(Node newNode) {
        // if no head
        if (this.top == null) {
            this.top = newNode;
            this.top.next = this.bottom;
        }
        // if no tail
        else if (this.tail == null) {
            this.bottom = newNode;
        }
        // if the tail is defined
        else if (this.bottom != null) {
            this.bottom.next = newNode;
            this.bottom = newNode;
        }

    }

    public Node dequeue() {
        Node front = null;
        // checks for the head to be there
        if (this.top != null) {
            front =  this.top;
            // updates the front
            this.top = this.top.next;
        }
        // returns the front node
        return front;
    }
}