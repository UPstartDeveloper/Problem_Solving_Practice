/*
 * Hacker Rank Problem found here:
 * https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup&isFullScreen=true
 */

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/* Assumptions Made in Solution:
 * the array of clouds always begins and ends with a cumulus cloud (0)
 */

/* Variable Trace Table
 * Variables  | currentIndex   |  jumps | jumpLength  |   c => Length: 6
 * Value      |     0          |   0    |    2        | [0, 0, 0, 1, 0, 0,]
 *            |     2          |   1    |    2        |
 */
public class Solution {

    /*
     * Pre: int[] c: integers representing the clouds to traverse
     * Post int jumps: minimum number of advances needed to reach last cloud
     */
    public static int jumpingOnClouds(int[] c) {
        // init currentIndex and jumps
        int currentIndex = 0, jumps = 0;
        // traverse the clouds
        while (currentIndex < c.length - 1){
            // find the number of clouds to advance on the next jump
            int jumpLength = 2;
            // switch jumpLength to 1 if we're going outside c,
            // or jumping onto a thunderhead
            int nextIndex = currentIndex + jumpLength;
            if (nextIndex >= c.length || c[nextIndex] == 1){
                jumpLength = 1;
            }
            // advance the player
            currentIndex += jumpLength;
            // increment jumps made
            jumps += 1;
        }
        // return the minimum number of jumps
        return jumps;

    }

    private static final Scanner scanner = new Scanner(System.in);
    /*
     * Pre: Scanner scanner: reads integers representing the clouds in the game
     * Post: None
     */
    public static void main(String[] args) throws IOException {
        //------------------------------------
        // Demonstrates use of while loops and
        // conditional statements
        //------------------------------------
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] c = new int[n];

        String[] cItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int cItem = Integer.parseInt(cItems[i]);
            c[i] = cItem;
        }

        int result = jumpingOnClouds(c);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
/*
 * Big O Complexity:
 * Time: This runtime of this solution rises asymptotically the amount of
         iterations made while traversing the array, which increases linearly
         with respect to the length of c. This in turn can be represented by the
         variable n, which allows us to express the runtime complexity as O(n).
         This is arguably the fastest runtime complexity for this problem, because
         we always need to traverse the array in some form, in order to know how
         many 0's and 1's there are, and at which indices in the array they are
         located.
 *
 * Space: This solution uses memory for local variables, meaning its space
          complexity is independent of the input. Therefore, the space complexity
          can be expressed as O(!).
 */
