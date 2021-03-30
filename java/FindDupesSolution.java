/* 
 * Find Duplicates: You have an array with all the numbers from 1 to N, 
 * where N <= 32,000.
 * 
 * The array may have duplicate entries and you do not know what N is. 
 * 
 * With only 4 kilobytes of memory available, 
 * how would you print all duplicate elements in the array?
 * 
 * Clarify:
 * 1) input is an array of ints? yes
 * 2) unsorted? yes
 * 3) pos/neg? both are possible
 * 4) and the goal is to print all the unique elements?
 * 5) does the output need to be in any order? no
 * 
 * Example I/O:
 * 
 *     0   1   2   3   4   5   6   7  8
 *  i  j
 *    [9   9  -6   4   1   1   3   6  5]
 *     l                              h
 * 
 * Intuition: eyes can find all the unique element
 *  - no scalable, error prone
 * Approach (memory):
 *  - frequency dist
 *  - dump it into a set
 * Approach (no ext mem)
 *  - sort the array (in-place)
 *  - print the number as it changes - 2 pointers
 * 
 * Edge Cases: 
 *  - empty array ---> do nothing
 *  
 * In-place Sorting algorithms - allowed to use built-in? nope
 * 
 * Others: 
 * insertion, bubble sort, selection sort, 
 * (quicksort - might seem like the best one, however we need to do it all in-place)
 *      - any assumption about the data beforehand - 
 *      - what would be the best choice of pivot if we use Quicksort?
 */

public class FindDupesSolution {
    public static int[] quickSort(int[] numbers) {
        int[] sorted = null;
        // A: base case
        if (numbers.length < 2) {
            sorted = numbers;
        }
        // B: sorting part
        return sorted;
    }
    public static void findDuplicates(int[] numbers) {
        // A: TODO: sort the array (using quicksort)
        int[] sorted = quickSort(numbers);
        // B: print unique elements
        printUnique(sorted);
    }
}
