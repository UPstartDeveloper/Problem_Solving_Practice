/* 
 *
 * Suppose you're given an unsorted array, a. The array is intended to have all integer elements between its minimum and maximum, but could be missing some elements. Write a python function to find the n-th missing element in the array.
 * Consider the array in sorted order, then find the n-th missing number. If the n-th missing number does not exist, you can output 'Does not exist'.
 * Examples:
 * Input: a = [2, 3, 11, 9], n = 3
 * Output: 6
 * Missing elements in array: [4, 5, 6, 7, 8, 10]. So, the 3rd missing element is 6.
 * 
 * Input: a = [2, 3, 5], n = 5
 * 0utput: 'Does not exist' 
 * Since there is no 5th missing element in the array, we output 'Does not exist' (the only missing element here is 4).
 * 
 * Brainstorm:
 * 
 * 1. Brute force = use nested for loops - quadratic
 *
 * 2. Sorting the array - linearithmic
 * 
 * 3. Set - linear (as a function of size of array, and range of elements)
 * 
 * Intuition - looking for the holes in ordered list, but given unordered collection
 * Approach: hybridize 2 and 3 -> only do 3 if range is close to n, otherwise do 2
 * Edge Cases: empty array, 
 *             array of values in reverse order, 
 *             array of all duplicates,
 *             no gaps
 *             n is not positive - assume it's not possible
 */

/** Template for writing Javadoc comments for methods 
 * 
 * /**
 * Short one line description.                           (1)
 * <p>
 * Longer description. If there were any, it would be    (2)
 * here.
 * <p>
 * And even more explanations to follow in consecutive
 * paragraphs separated by HTML paragraph breaks.
 *
 * @param  variable Description text text text.          (3)
 * @return Description text text text.
 * */


import java.lang.Integer;
import java.util.Arrays;  // builtin sorting, and typecasting to List interface
import java.util.Collections; // built-in min() and max() functions
import java.util.HashSet;


public class NthMissing {
    public static int setSolution(int[] nums, int n) {
        /**  
         * Finds the nth missing value from unsorted array of integers via a HashSet.
         * 
         * For example, when nums = [2, 3, 11, 9] and n = 3, we return 6.
         * This is b/c we first sort the nums array. Then find the missing values, and sort them.
         * That gives us the values [4, 5, 6, 7, 8, 10]. Finally, we return the the 3rd value 
         * from that collection of integers, 6.
         * 
         * @param nums the array of unsorted integers.
         * @param n    the index of the number to return, from the missing values when they are in sorted order. 
         * 
         * @return     int is the n-th missing value is found, otherwise null.
         */
        /**
         * Time: O(nums + range); 
         * Space: O(nums)
         */
        // init output
        int answer = null;
        // validate input
        if (nums.length > 0 && n > 0) {
            // get the min and max
            Integer[] ints = Arrays.copyOf(nums, nums.length);
            int min = Collections.min(Arrays.asList(ints));
            int max = Collections.max(Arrays.asList(ints));
            // make a set of all values in the array
            HashSet<Integer> presentNums = new HashSet<Integer>();
            for (int num: nums) {
                presentNums.add(num);
            }
            // iterate over the missing values
            int currentVal = min;
            int missingValues = 0;
            while (currentVal < max + 1) {
                // see if the value is there
                if (presentNums.contains(currentVal) == false) {
                    missingValues += 1;
                }
                // if found, update the answer 
                if (missingValues == n) {
                    answer = currentVal;
                    break;  // and exit the loop
                }
                // or move on to the next value
                currentVal += 1;
            }
        }
        return answer;
    }

    public static int sortingSolution(int[] nums, int n) {
        // init output
        int answer = null;
        // validate input
        if (nums.length > 0 && n > 0) {
            // sort the array in place
            Arrays.sort(nums);
            // iterate over the array 
            Integer[] ints = Arrays.copyOf(nums, nums.length);
            int min = Collections.min(Arrays.asList(ints));
            int max = Collections.max(Arrays.asList(ints));
            int missing = 0, expected = min;
            for (int index = 0; index < nums.length; index += 1) {
                int num = nums[index];
                // don't find a missing value
                if (num == expected) expected += 1;
                // if expected is not found - inch closer to answer
                else missing += 1;
                // if missing found, update the answer
                if (missing == n) return expected;
            }
        }
        // if invalid input, return null
        return answer;
    }
    

    // TODO: implement main method
}
