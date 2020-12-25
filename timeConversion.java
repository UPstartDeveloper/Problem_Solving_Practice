/* copying the imports from the Hacker Rank problem description:
 * https://www.hackerrank.com/challenges/time-conversion/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
 */
import java.io.*;
// import java.util.*;

public class timeConversion {

    /*
     * calculateNewHour
     * pre: String time is a time given in 12-hour AM/PM format,
     *      i.e. '07:23:45AM' or '10:36:55PM'
     * post: String newHour is a two character that represent the equivalent
             hour for 24-format. It is between 0-24
     */
     public static String calculateNewHour(String time) {
         // initial conversion (that works for most PM times)
         int currentHour = Integer.parseInt(time.substring(0, 2));
         // determine and perform any conversion if needed
         if ((time.contains("AM") && currentHour == 12) ||
             (time.contains("PM") && currentHour != 12)) {
             currentHour += 12;
         }
         // initialize output value
         String newHour = String.valueOf(currentHour);
         // if necessary to make 2 characters long, then we add zero to output
         if (newHour.length() == 1) {
             newHour = "0" + newHour;
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
    static String convertTime(String time) {
        // declare output value
        String twentyFour = "";
        // store the subset of characters in s that are the same in output
        String common = time.substring(2, 8);
        // calculate what the hour of twentyFour should be
        String newHour = calculateNewHour(time);
        // combine the new hour with old minutes and seconds
        twentyFour = newHour + common;
        return twentyFour;
    }
    /*
     * Scanner instance and main method are inspired by tbe starter
     * on Hacker Rank (same link as above):
     * https://www.hackerrank.com/challenges/time-conversion/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
     */
    // private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        String timeAM = "12:40:03AM";
        // String timePM = "12:56:34PM";
        System.out.println(convertTime(timeAM));

    }
}
