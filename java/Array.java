import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Integer;
import java.lang.Math;
import java.util.Iterator;
import java.util.Hashtable;

public class Array {

    public int linearSearch(ArrayList<Integer> list, int target) {
        int index = 0;
        while (index < list.size()) {
            if (list.get(index) == target) {
                return index;
            }
            index += 1;
        }
        return -1;
    }

    /* Differences between the HashMap and HashTable:
     * Hashtable is older
     * HT is thread-safe and sync'd
     * HT is slower
     * HT works w/ multiple languages
     * HT doesn't allow null as a key
     */

    public int binarySearchIterative(ArrayList<Integer> list, int target) {
        // ASSUMES the list is sorted
        int low = 0, hi = list.size() - 1;
        while (low <= hi) {
            // find the middle
            int midIndex = Math.floorDiv(low + hi, 2);
            int midElem = list.get(midIndex);
            // target found
            if (target == midElem) {
                return midIndex;
            }
            // go left
            else if (target < midElem) {
                hi = midIndex - 1;
            }
            // go right
            else {
                low = midIndex + 1;
            }
        }
        // not found
        return -1;
    } 

    public static boolean twoSum(int[] nums, int target) {
        /* returns true if two numbers exist in the array such that 
         * the target sum can be found
         * note that this is CONTRIVED just to get practice using Java
         * data structures
         */
        boolean found = false;

        // A: init a HT
        Hashtable<Integer, Integer> numPairs = new Hashtable<Integer, Integer>();
        // B: iterate over the array
        for (int num: nums) {
            // C: compute the remaining number needed to make the sum
            int pair = target - num;
            numPairs.put(num, pair);
        }
        // D: iterate over the HT key value pairs
        Iterator<Integer> numbers = numPairs.keySet().iterator();
        while (numbers.hasNext() == true) {
            // E: check if the diff is another one of the key value pairs
            int num = numbers.next();
            int pair = numPairs.get(num);
            if (numPairs.containsKey(pair)) {
                found = true;
            }
        }
        
        return found;
    }

    public static int[] mergeArrays(int[] left, int[] right) {
        /* 
         * m = [3, 4]
         * lN = 1, rightN = 0
         *  [3]      [4]
         * mN = 1;
         */
        int leftNdx = 0, rightNdx = 0;
        int[] merged = new int[left.length + right.length];
        int mergedNdx = 0;
        // A: array elems battle positions in the merged arr
        while (leftNdx < left.length && rightNdx < right.length) {
            int leftElem = left[leftNdx], rightElem = right[rightNdx];

            if (leftElem <= rightElem) {
                merged[mergedNdx] = leftElem;
                leftNdx += 1;
            } else {
                merged[mergedNdx] = rightElem;
                rightNdx += 1;
            }
            mergedNdx += 1;
        }
        // B: add any left overs
        while (leftNdx < left.length) {
            merged[mergedNdx] = left[leftNdx];
            leftNdx += 1;
            mergedNdx += 1;
        }
        while (rightNdx < right.length) {
            merged[mergedNdx] = right[rightNdx];
            rightNdx += 1;
            mergedNdx += 1;
        }
        // c: return the merged array in sorted order
        return merged;
    }

    public static int[] mergeSort(int[] numbers) {
        /*
         * Divide: find the middle of the array Conquer: sort the left and right
         * Combine: merge the sorted lists together
         *            0  1  2  3  4  5
         * numbers = [1, 3, 4, 4, 5, 6]
         * midNdx = 6 // 2 = 3
         * sortedLeft = [1, 3, 4]
         * sortedRight
         *                
         */

        // BASE: small array
        System.out.println(Arrays.toString(numbers));
        if (numbers.length < 2) {
            return numbers;
        } else {
        // RECURSIVE: merge sort algo
            int midNdx = Math.floorDiv(numbers.length, 2);
            int[] sortedLeft = mergeSort(Arrays.copyOfRange(numbers, 0, midNdx));
            int[] sortedRight = mergeSort(Arrays.copyOfRange(numbers, midNdx, numbers.length));
            return mergeArrays(sortedLeft, sortedRight);
        }

    }

    public static void main(String[] args) {
        int[] nums1 = {1, 3, 4, 5, 6, 4};
        int[] nums2 = {1};
        int[] targets = {11, 3};
        System.out.println(twoSum(nums1, targets[0]));
        System.out.println(twoSum(nums2, targets[1]));
        System.out.println(Arrays.toString(mergeSort(nums1)));
    }
}