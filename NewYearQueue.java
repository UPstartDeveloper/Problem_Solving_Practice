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
  */

 public class NewYearQueue{
    static void minimumBribes(int[] q) {
        int swaps = 0;
        boolean isChaotic = false;
        for (int i = 0; i < q.length; i++){
            int element = q[i];
            int difference = element - i;
            // the element is not impossible to exist at that space
            if (difference > 3){
                isChaotic = true;
            } else if (difference >= 2){ // contribute number of swaps
                swaps += difference - 1;
            }
        }
        if (isChaotic == true){
            System.out.println("Too chaotic");
        } else {
            System.out.println(swaps);
        }
    }

    public static void main(String[] args) {
       //TODO
    }
 }