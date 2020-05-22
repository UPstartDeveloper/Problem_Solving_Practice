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

public class Solution {

    /*
     * Pre: int[] c: integers representing the clouds to traverse
     * Post int jumps: minimum number of advances needed to reach last cloud
     */
    public static int jumpingOnClouds(int[] c) {


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
