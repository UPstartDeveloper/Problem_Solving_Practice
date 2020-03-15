/* copying the imports from the Hacker Rank problem description:
 * https://www.hackerrank.com/challenges/time-conversion/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
 */
import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * calculateNewHour
     * pre: String hourInPM has two digits that represent a number 1-12, and
            is for a time in the PM format
     * post: String newHour is a two character that represent the equivalent
             hour for 24-format. It is between 13-23, and includes 0 as well.
     */
     public static String calculateNewHour(String hourInPM) {
         // convert the hour using integers
         int currentHour = Integer.parseInt(hourInPM) + 12;
         // convert to 00 if necessary
         if (currentHour == 24) {
             currentHour = 0;
         }
         String newHour = String.valueOf(currentHour);
         // add an extra 0 to the output if necessary
         if (newHour.length() == 1) {
             newHour = "00";
         }
         return newHour;
     }
    /*
     * timeConversion
     * pre: String time is a time given in 12-hour AM/PM format,
     *      i.e. '07:23:45AM' or '10:36:55PM'
     * post: String twentyFour is the equivalent of s in 24-hour format,
     *      i.e. '07:23:45' or or '22:36:55PM'
     */
    static String timeConversion(String time) {
        // declare output value
        String twentyFour = "";
        // determine if s is a AM or PM time
        String amOrPM = time.substring(8);
        if (amOrPM.startsWith("A")) {
            // return the same time without the AM piece
            twentyFour = time.substring(0, 8);

        } else { // time is in PM
            // store the subset of characters in s that are the same in output
            String common = time.substring(2, 8);
            // calculate what the hour of twentyFour should be
            String hourInPM = time.substring(0, 2);
            String newHour = calculateNewHour(hourInPM);
            // combine the new hour with old minutes and seconds
            twentyFour = newHour + common;

        }
        return twentyFour;

    }

    /*
     * Scanner instance and main method are inspired by tbe starter
     * on Hacker Rank (same link as above):
     * https://www.hackerrank.com/challenges/time-conversion/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
     */
    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        String timeAM = "12:56:34AM";
        String timePM = "12:56:34PM";
        System.out.println(timeConversion(timeAM));

    }
}
