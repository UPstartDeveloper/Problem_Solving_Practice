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
     public static void printStaircase(int steps)
     {

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
         System.out.println("Here You Go! Have Fun and Reach Your Dreams!");
         printStaircase(steps);

     }
 }
