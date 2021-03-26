import java.util.ArrayList;
import java.lang.Error;

class Deque {
    ArrayList<Integer> items;
    String errorMsg = "There are no items to return.";

    // constructor
    public Deque(ArrayList<Integer> collection) {
        this.items = collection;
    }

    public void append(int value) {
        // adds element to the end of the collection
        this.items.add(value);
    }

    public void appendLeft(int value) {
        // adds the element to the beginning of the collection
        this.items.add(0, value);
    }

    public int popLeft() {
        if (this.items.size() > 0) {
            // return the first item
            return this.items.remove(0);
        } else {
            // raise an error
            throw new Error(this.errorMsg);
        }
    }
    
    public int pop() {
        if (this.items.size() > 0) {
            // return the last item
            int lastIndex = this.items.size() - 1;
            return this.items.remove(lastIndex);
        } else {
            // raise an error
            throw new Error(this.errorMsg);
        }
    }
}