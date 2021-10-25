import javax.xml.namespace.QName;

/**
 * ITERATOR DESIGN PATTERN (OOP): 
 * int[] arr = [1, 2, 3]; 
 * Iterator<Integer> it = arr.iterator(); 
 * while(it.hasNext()){ 
 *      print it.next(); 
 * } // output: 123 
 * 
 * hasNext() // returns whether or not the iterator has additional elements 
 * 
 * next() // returns
 * next element in iterator, throws NoSuchElementException otherwise.
 * ---------------------------------------------------- 
 * CHALLENGE: Given an
 * iterator of iterators, implement an interleaving iterator that takes in: 
 * 
 * - an iterator of iterators, and
 * 
 * output: elements from the nested iterators in interleaved order.
 * 
 * That is, if we had the iterators i and j iterating over the elements 
 * [ ia, ib, ic] and [ja, jb] respectively,
 * 
 * the order in which your interleaving iterator should emit the elements would
 * be [ia, ja, ib, jb, ic].
 * 
 * Your interleaving iterator should: 
 * - implement the Iterator interface, 
 * - take in the iterator of iterators in its constructor
 * - and provide the 
 *      next() and
 *      hasNext() methods.
 * 
 * Assume that there are no additional methods offered by the iterator.
 * 
 * 
 * Given the following three iterators put into an array of iterators…
 * 
 * int[] arr1 = [1, 2, 3]; int[] arr2 = [4, 5]; int[] arr3 = [6, 7, 8, 9];
 * [      0  1  2  3
 * 0     [1, 2, 3], F
 * 1     [4, 5],    F
 * 2     [6, 7, 8, 9] T
 * ]
 * this.currentIteratorIndex = 0 --> 2
 * [1, 2, 3]; int[] arr2 = [4, 5]; int[] arr3 = [6, 7, 8, 9];
 * Iterator<Integer> a = arr1.iterator(); Iterator<Integer> b = arr2.iterator();
 * Iterator<Integer> c = arr3.iterator(); Iterator<Integer>[] iterlist = [a, b,
 * c];
 * 
 * IF itfl = new IF(iterlist); 
 * while(IF.hasNext()){ 
 * print IF.next(); } // 1 4 6
 * 2 5 7 3 8 9
 * 
 * class IF{ public IF(Iterator<T>[] iterlist){ } public T next(){ }
 * 
 * public boolean hasNext(){ } }
 * 
 * Clarifications: 
 * - ASSUME we can use the built-in iterator interface? -
 * - PROBLEM: basically print items at corresponding indices in all the iterators
 * we've got? 
 * - CANNOT assume the iterators are of the same length --> if a list doesn't have it, just leave it out 
 * - ASSUME the order of the iterators in the array passed to constrcutor --> determines their order 
 * - ASSUME that iterators passed in are 1D
 * 
 * Intuition: 
 *      - print items at corresponding indices in all the iterators
 * 
 * Approach
 * 
 * Edge Cases:
 *      - iterators of uneven length what to do when we go beyond one
 *      - duplicates -- not a problem
 */

import java.util.Iterator;

public class IF{ 
    Iterator<T>[] iterlist = null;

    public IF(Iterator<T>[] iterlist){
        this.currentIteratorNdx = 0;
        this.iterList = iterlist;
    } 

    public T next(){ 
        /**
         * Assume it only prints 1 element at a time,
         * and that hasNext is already True
         * for each of the Iterators in the
         * array which hasNext is true
         */ 
        // get the next element to return
        T nextElement = this.iterList[this.currentIteratorNdx].next();
        // move to the next iterator (staying in bounds)
        this.currentIteratorNdx = (this.currentIteratorNdx + 1) % this.iterList.length;
        // return the next element
        return nextElement;
    }

    private int getNextAvailableIterator() {
        /** starting from the current index we have, 
         * let's circle around the list of iterators
         * to try and find one that has another item available.
         * 
         * If not found, we'll just return -1
         */

        int currentIndex = this.currentIteratorNdx;
        int maxChecks = this.iterList.length;
        int checksSoFar = 0;
        while (checksSoFar < maxChecks) {
            // check the iterator
            Iterator it = this.iterList[currentIndex];
            // if available, return its index
            if (it.hasNext() == true) {
                return currentIndex;
            }
            // if not, move on to the next
            currentIndex = (currentIndex + 1) % this.iterList.length;
            checksSoFar += 1;
        }
        // if not found, return -1
        return -1;

        /**
         * 
         
        // linear search for the iterator we can get a next element from
        for(int i = this.currentIteratorNdx; i < this.iterList.length; i += 1) {
            Iterator it = this.iterList[i];
            if (it.hasNext() == true) {
                return i;
            }
        }
        return -1;
        */
    }

    public boolean hasNext(){ 
        // if any of the iterators have more items, return True
        if (this.currentIteratorNdx < this.iterList.length) {
            // get the index of the next available iterator
            int nextAvailable = this.getNextAvailableIterator();
            // return true if one is found
            if (nextAvailable > -1) {
                this.currentIteratorNdx = nextAvailable;
                return true;
            }
        }
        return false;
    } 
}