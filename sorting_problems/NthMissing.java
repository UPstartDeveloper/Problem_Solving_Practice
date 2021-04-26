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
 */


import java.util.Arrays;
import java.util.HashSet;


public class NthMissing {
    // TODO: implement solution

    // TODO: implement main method
}
