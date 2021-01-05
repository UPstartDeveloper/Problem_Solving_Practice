/* In this problem,
 * we are given an array of integers that represents the prices of a stock.
 * The values are sorted by the date.
 * 
 * Our job is to find the largest increase in the stock over time, or to return
 * 0 if the stock is strictly decreasing and/or stagnant in value.
 */

import java.lang.Integer;


public class StockRise {
    
    public static int getLargestIncrease(int[] prices) {
        /* Big O Analysis
         * Time is O(n)
         * Space is O(1)
         */
        // A: init the largest difference at 0
        int largestIncrease = 0;
        int smallestSoFar = Integer.MAX_VALUE;
        // B: linearly search for the largest increase
        int index = 0;
        while (index < prices.length) {
            int price = prices[index];
            // Case 1: this is the smallest number so far
            if (price < smallestSoFar) {
                smallestSoFar = price;
            } else {
            // Case 2: otherwise this could be our largest increase so far
                int difference = price - smallestSoFar;
                // update the answer as appropiate
                if (difference > largestIncrease) {
                    largestIncrease = difference;
                }
            }
            // move on in the prices array
            index += 1;
        }
        // C: return the answer
        return largestIncrease;
    }
    public static void main(String[] args) {
        // test case 1
        int prices1[] = { 1 }; // output 0
        System.out.println("The answer to 1 is: " + getLargestIncrease(prices1));
        // test case 3
        int prices3[] = { 1, 1, 1, 1, 1 }; // output 0
        System.out.println("The answer to 3 is: " + getLargestIncrease(prices3));
        // test case 6
        int prices6[] = { 0, -1, -2 }; // output 0
        System.out.println("The answer to 6 is: " + getLargestIncrease(prices6));
        // test case 2
        int prices2[] = { 1, 2, 3, 4, 5, 6 }; // output 5
        System.out.println("The answer to 2 is: " + getLargestIncrease(prices2));
        // test case 4
        int prices4[] = { -7, 8, 10, 2, 13, -14 }; // output 20
        System.out.println("The answer to 4 is: " + getLargestIncrease(prices4));
        // test case 5
        int prices5[] = { 2, 8, 10, -7, 13, -14 }; // output 20
        System.out.println("The answer to 5 is: " + getLargestIncrease(prices5));
    }
}