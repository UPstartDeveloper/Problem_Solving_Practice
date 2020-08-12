/* Solution for "Maximum of Subarrays", Problem #62 on Data Interview Q's
 * 
 * Problem Statement
 * Given an array and an integer A, find the maximum for each contiguous subarray of size A.
 * Input: array = [1, 2, 3, 1, 4, 5, 2, 3, 6], A = 3
 * Output: 3 3 4 5 5 5 6   
 * Below is a more detailed walkthrough of what you should be trying to code, using the example above:

    subarray 1 = [1, 2, 3,
    maximum of subarray 1 = 3
    subarray 2 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    maximum of subarray 2 = 3
    subarray 3 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    maximum of subarray 3 = 4
    Etc.
 */

import java.lang.Integer;

 public class MaxSubArray{
    /* pre: array of integers, integers for the starting and stop index
            of the subarray we want to traverse
     * post: the largest integer, found through linear search
     */
    public static int findMax(int[] array, int start, int stop){
       int maximum = Integer.MIN_VALUE;
       // linear search for the maximum in the subarray
       for(int i = start; i < stop; i++){   // A iterations (A = stop - start)
          // prevent indexing errors
          if(i < array.length){
            int num = array[i];
            // replace the maximum if necessary
            if (num > maximum)  
               maximum = num; 
          }
       }
       return maximum;
    }
    /* Pre: nums is an array of integers, and subSize is the 
            size of each subarray we want to find the maximum for
     * Post: None. The maximum values are printed to standard output
     */
     public static void solution(int[] nums, int subSize){
        // Idea #1: iterate through the list
        for(int index = 0; index <= nums.length - subSize; index += 1){  // n iterations
            // find the maximum value of the subarray
            int maxNum = findMax(nums, index, index + subSize);  // A iterations
            // print the maximum value
            System.out.print(maxNum + " ");  // O(1)
        }       
     }
    /* Pre: None
     * Post: the max values for each subarray are printed to standard output
     */
     public static void main(String[] args){
        // execution on test input above
         int[] nums = {1, 2, 3, 1, 4, 5, 2, 3, 6};
         int subSize = 3;
         solution(nums, subSize);
     }
 }


/* Variable-Value Trace:
 * just to demo how the algorithm works, let's look at the
 * first two iterations of the for loop in the solution() method:
 * nums = [1, 2, 3, 1, 4, 5, 2, 3, 6]
 * start |  stop  |  max  |  i   |  num
 *   0       3       MIN     0       1
 *                    1      1
 *                    2      2
 *                    3  
 * print(3)
 *   1       4       MIN      1      2
 *                    2       2      3
 *                    3       3      1
 * print(3)
 * ...
 * 
 * Complexity Analysis:
 * Time O(n * A), where n = length of input numbers, and 
 *                      A = length of sub array to find maximum of
 * Constant Memory - because we just print the maximums to standard output,
 *                   and we use the same array object to find maximums
 * 
 * ...
 *     
 * Suggestions for Improvement:
 * 
 * - OOP: I could make the array and A both properties of the class
 * - Time: a key insight to this problem is that the maximum of a sub array
 *         is only different from the maximum of the previous, if the last 
 *         element at the end of the new subarray is higher than the maximum
 *         of the previous subarray.
 *         
 *         Refactoring the solution to utilize this idea would speed up the
 *           program, by reducing the number times we do linear search to 
 *           find the maximum of a subarray. However, before implementing 
 *           it in code I would need to consider what to do in edge case where
 *           we move to a subarray, and the new element at the end is less than
 *           the maximum of the previous subarray; BUT that maximum value 
 *           is no longer in the subarray anymore, so it's not a valid integer
 *           to compare to. This is what makes the current solution more robust,
 *           albeit naive.
 */