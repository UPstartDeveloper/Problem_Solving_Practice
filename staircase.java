import java.util.Scanner;


public class Staircase {
    //-----------------------------------------------------
    // Solution to the Hacker Rank problem found here:
    // Solving the Hacker Rank problem found below::
    // https://www.hackerrank.com/challenges/staircase/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
    //-----------------------------------------------------

    /**********************************************************************
     * printStaircase
     * pre: int steps is number of steps in the staircase
     * post: prints a right-aligned staircase with steps number of rows,
     *       and an increasing number of # symbols going down the rows
     *********************************************************************/
     public static void printStaircase(int stepNum)
     {
         //  # initialize a count of symbols to print on each step of the staircase
         int quota = 1;
         // build the representation of the steps using # symbols and spaces
         for (int i = 0; i < stepNum; i+=1) {
             String step = "";
             for (int j = 0; j < stepNum; j++) {
                 // print spaces until it is time to add # to the output line
                 if (stepNum - j <= quota) {
                     step += "#";
                 } else {
                     step += " ";
                 }
             }
             // display the output
             System.out.println(step);
             // increment the number of symbols needed for the next iteration
             quota += 1;
         }
     }

     /*******************************************************************
     * Driver method
     * pre: None
     * post: invokes the printStaircase method once and passes in input
     *       from user
     *********************************************************************/
     public static void main(String[] args)
     {
         // take input from user on number of steps
         Scanner scan = new Scanner(System.in);
         System.out.print("Enter number of step in staircase: ");
         int steps = scan.nextInt();

         // printing the staircase
         System.out.println("------------------------------------------------");
         System.out.println("Here You Go! Have Fun and Climb For Your Dreams!");
         printStaircase(steps);

     }
 }
