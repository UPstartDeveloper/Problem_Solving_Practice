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
        // A: init the largest difference at 0
        int largestIncrease = 0;
        int smallestSoFar = Integer.MAX_VALUE;
        // B: use two pointers to linearly search for the largest increase
        int firstNumIdx = 0;
        while(firstNumIdx < prices.length) {
            // C: get the first number
            int firstNum = prices[firstNumIdx];
            // replace the smallest if appropaite
            if (firstNum < smallestSoFar) {
                smallestSoFar = firstNum;
            }
            // D: move ahead to the next largest foreseeable number
            int secondNumIdx = firstNumIdx + 1;
            while(secondNumIdx < prices.length - 1 && prices[secondNumIdx + 1] > firstNum) {
                secondNumIdx += 1;
            }
            // E: calculate the difference
            if (secondNumIdx < prices.length) {
                int currentIncrease = prices[secondNumIdx] - smallestSoFar;
                // F: and update the answer as necessary
                if (currentIncrease > largestIncrease) {
                    largestIncrease = currentIncrease;
                }
            }
            // G: move ahead the firstNum's pointer
            firstNumIdx = secondNumIdx;
        }
        // H: return the answer
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