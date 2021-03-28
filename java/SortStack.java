/* 
 * Write a program to sort a stack such that the smallest items are on the top. 
 * You can use an additional temporary stack, 
 * but you may not copy the elements into any other data structure (such as an array). 
 * The stack supports the following operations: 
 * push, 
 * pop
 * peek,
 * isEmpty.
 * 
 * Clarifications:
 * 1) So rearranging the stack? yes
 *      Data values - assume Integers
 *      REQUIRES DSBS
 * 2) pop - err handling? yes
 * 3) size constraints? nope
 * 4) is whole stack sorted? yes
 *      - different from a MinHeap
 * 5) ASSUME unsorted stack
 *  ArrayStack
 *  b         t
 *  [  6, 7, 8, 8, 1, 5, 10       ]
 *  0       n-1
 * 
 * rearrange
 * 
 *   b                    t
 *  [ 10, 8, 8, 7, 6, 5, 1 ]
 *  0                   n-1
 *  
 * Intuition:
 *  - the SortStack seems very similar to a MinHeap - but whole thing is sorted
 * Approach:
 *      1) ArrayStack, temporary stack
 *          - purpose of temp is sort all items such that top -> bottom, DESC order -> 
 *                 pop back onto the first stack
 *          - allowed to index into an ArrayStack? - if yes, just implement insertion/merge/quicksort algo
 *                      0  1  2  3  4  5  6
 *          - stack: [  ]
 *          - indices = {4, 5, 0, 1, 2, 3, 6}
 *          - temp: [1, 5, 6, 7, 8, 8, 10]
 * 
 *          Brute Force:
 *              - ASSUME iteration is ok
 *              - selection sort
 *              // init a temp ArrayStack
 *              // find the next smallest stack elem, for n times (linear search)
 *                  // add to the temp
 *                  // record the index where it came from
 *              // empty the original stack
 *              // empty the temp --> original
 *      2) MinStack?
 *          stack [  6, 7, 8, 8, 1, 5, 10       ]
 *          mins 
 *      
 * 
 */


import java.lang.Integer;
import java.util.ArrayList;
import java.util.HashSet;


public class Solution {
    // TODO: make rest of methods
    ArrayList<Integer> nums;

    public Solution(ArrayList<Integer> nums) {
        this.nums = nums;
    }

    public ArrayList<Integer> sortStack() {

        // A: init a temp ArrayStack, and recorded indices - TODO: make a helper
        int[] temp = new int[this.nums.size()];
        int tempNdx = 0;
        HashSet<Integer> indices = new HashSet<Integer>();
        // for n times (linear search) -- O(n^2)
        while (tempNdx < temp.length) {
            int lowestElem = Integer.MAX_VALUE, lowestNdx = -1;
            for (int stackNdx = 0; stackNdx < this.nums.size(); stackNdx += 1) {
                // find the next smallest stack elem, 
                if (indices.contains(stackNdx) == false) {
                    int stackElem = this.nums.get(stackNdx);
                    if (stackElem < lowestElem) {
                        lowestElem = stackElem;
                        lowestNdx = stackNdx;
                    }
                }
            // add to the temp
            temp[tempNdx] = lowestElem;
            tempNdx += 1;
            // record the index where it came from
            indices.add(lowestNdx);
            }
        }
        // B: empty the original stack - TODO: make a helper
        this.nums.clear();  // O(n)
        // C: empty the temp --> original -- O(n)
        for (int index = temp.length - 1; index > 0; index -= 1) {
            int elem = temp[index];
            this.nums.add(elem);
        }
        // DONE!
        // Time: O(n^2)
        // Space: O(n)

    }
}

/* TEST
 *         0  1  2  3  4  5  6      7 - end condition
 * nums: [10, 8, 8, 7, 6, 5, 1]
 *                            v 
 * t:    [ 1  5, 6, 7, 8, 8, 10 ]
 * tNdx:      ^
 * sNdx:   ^ 
 * i's:  { 4, }
 * lE:     1
 * lNdx:   4
 * sE:     6
 */