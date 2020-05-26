/* 
 * Hacker Rank problem found here:
 * https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays&isFullScreen=true
 */

 /*
  * Idea 1: take into account the relationships between indices and elements
  *         at SINGULAR positions in the array
  *     
  *     A: Iterate over the array
  *        a. if the element is greater than its index by more than 3,
                it's too chaotic,
  *        b. otherwise if the element is greather than its index by at least 2,
                increment the number of swaps by 1 less than the difference
  *
  * Observations:
  * it is possible for an element to go ahead of another element that is much smaller than it;
  * HOWEVER any one element will always be found within 2 positions of where it should be (index + 1)
  * it is assumed that each element only moves in one direction, from where their original index was
  * 
  * Idea 2: using the differences between adjacent elements
  *     A: iterate over the array
  *         a. deciding it's too chaotic is the same
            b. otherwise, the way we calculate the number of bribes is the following:
                whenever two elements are out of place, we increment bribesCount by their difference
  */

 public class NewYearQueue{
    static void minimumBribes(int[] q) {
        /*
         * The following solution was implemented uaing inspiration from the C++ solution
         * mariogerbach posted in the Hacker Rank discussions of the problem:
         * https://www.hackerrank.com/challenges/new-year-chaos/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
         */
        int bribes = 0;
        boolean isChaotic = false;
        int expectedFirst = 1, expectedSecond = 2, expectedThird = 3;
        for (int i = 0; i < q.length - 1; i++){
            int element = q[i];
            // increment the expected values and the bribes as appropiate
            if (element == expectedFirst) {
                expectedFirst = expectedSecond;
                expectedSecond = expectedThird;
                expectedThird += 1;
            } else if (element == expectedSecond) {
                expectedSecond = expectedThird;
                expectedThird += 1;
                bribes += 1;
            } else if (element == expectedThird) {
                expectedThird += 1;
                bribes += 2;
             // check if the element makes the array too chaotic
            } else {
                isChaotic = true;
            }
         }
        if (isChaotic == true){
            System.out.println("Too chaotic");
        } else {
            System.out.println(bribes);
        }
    }

    public static void main(String[] args) {
       //TODO
    }
 }