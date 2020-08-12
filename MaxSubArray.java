/* Solution for "Maximum of Subarrays", Problem #62 on Data Interview Q's
 * 
 * Problem Statement
 * Given an array and an integer A, find the maximum for each contiguous subarray of size A.
 * Input: array = [1, 2, 3, 1, 4, 5, 2, 3, 6], A = 3
 * Output: 3 3 4 5 5 5 6
 * Below is a more detailed walkthrough of what you should be trying to code, using the example above:

    subarray 1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    maximum of subarray 1 = 3
    subarray 2 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    maximum of subarray 2 = 3
    subarray 3 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    maximum of subarray 3 = 4
    Etc.
 */

import java.lang.Integer;

 public class MaxSubArray{
    /* pre: array of integers
     * post: the largest integer, found through linear search
     */
    public static int findMax(int[] subArray){
       int maximum = Integer.MIN_VALUE;
       for(int num: subArray){
          if (num > maximum)
            maximum = num;
       }
       return maximum;
    }
    /* Pre: nums is an array of integers, and subSize is the 
            size of each subarray we want to find the maximum for
     * Post: None. The maximum values are printed to standard output
     */
     public static void solution(int[] nums, int subSize){
         
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