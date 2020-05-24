import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class birthdayCandles {
    /*************************************************************************
    // Solving "Brithday Cake Candles" problem on Hacker Rank:
    // https://www.hackerrank.com/challenges/birthday-cake-candles/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
    **************************************************************************/
    /* birthdayCakeCandles
     * Pre: int[] candleHeights is an array of the heights of brithday candles
     * Post: int - represents the number of candles that will go out
     *       by storing the occurences of the highest candle height
     */
     public static int birthdayCakeCandles(int[] candleHeights) {
        // form a hisotogram of the candles heights, using a HashMap
        HashMap<Integer, Integer> candles = new HashMap<Integer, Integer>();
        // simultaneously, determine the largest candle height
        int maxHeight = 0;
        for(int i = 0; i < candleHeights.length; i++) {
            // grab the height
            int height = candleHeights[i];
            // update maxHeight if appropiate
            if (height > maxHeight) {
                maxHeight = height;
            }
            // grab the current count associated with that height
            //int count = candles.get(height);
            if (candles.get(height) == null) {
                // if the height has not been seen before
                candles.put(height, 1);
            } else {
                // otherwise increment the current value
                candles.replace(height, candles.get(height) + 1);
            }
        }
        // return the occurences of the largest candle height
        return candles.get(maxHeight);
     }
     /* Main method
      * Pre: none
      * Post: none
      */
    public static void main(String[] args) throws IOException {
        int[] candleHeights = {3, 2, 1, 3};
        int candlesBlownOut = birthdayCakeCandles(candleHeights);
        System.out.println("Congrats! Your little sister is turning 4." + "\n" +
                            "Today she blew out: " + candlesBlownOut + " candles.");
    }

}

