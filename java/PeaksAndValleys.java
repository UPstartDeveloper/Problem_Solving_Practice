/* Problem:
 * 
 * Peaks and Valleys: In an array of integers, 
 * a "peak" is an element which is greater than or equal to the adjacent integers 
 * and a "valley" is an element which is less than or equal to the adjacent integers. 
 * For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. 
 * 
 * Given an array of integers, sort the array into an alternating sequence of peaks and valleys.
 * EXAMPLE
 * Input: {5, 3, 1, 2, 3}
 *         {5, 1, 6, 3 3}
 * Output: {5, 1, 3, 2, 3}
 * 
 * Clarification:
 * 0. array can be unsorted to begin with
 *  1. A peak --> +1 ints long? 
 *      - yes
 *      - goal is to get the p & v --> 1 int (but are duplicates allwed)
 * 2. all relative?
 *      - multiple ans
 * 3. pos + neg? yes
 * 4. size constraints? nope
 * 5. input modifiable? or should we do it out of place?
 *      - input is modifiable?
 * 6. can an elem be both a peak and a valley - nope
 * 7. 
 * 
 * Intuition:
 *      - 
 * Approach: 
 *      - naive:
 *          - {5, 3, 1,2, 3}
 *          A: sort the array
 *           {1, 2, 3, 3, 5}
 *            1, 3, 2, 5 ,3 
 *          B1: swap every element w/ its neighbor, skip one, repeat
 *          {1, 2, 3, 3, 5}
 *           ^     ^
 *           s1    s2
 *          {2, 1, 3, 3, 5} 
 *                       ^  // special case for end elem - swp w/ elem b4
 *          {2, 1, 3, 5, 3} 
 *          B2: swap elements from the ends
 *          {1, 2, 3, 3, 5}
 *           ^           ^
 *          {5, 2, 3, 3, 1}
 *              ^     ^
 *          {5, 3, 3, 2, 1}
 *          
 *          { 1 , 2}
 *          {3, 2, 1}
 *           ^  ^
 *          {2, 3, 1}
 * 
 *          {1, 2, 3}
 *          2, 1, 3
 * 
 *          {1, 2, 3, 3}
 *          {2, 1, 3, 3}
 *           p  v  p
 *              <= >
 *          {1, 2, 3, 3, 5}
 *           ^  ^
 *          {2, 1, 3, 3, 5}
 * 
 *          {2, 1, 3, 5, 3}
 * 
 *  Approach:
 *      - if an elem expected >= previous --> swap previous element forwards
 *      - if an elem expected <= previous --> swap previous element forwards
 */                      

public class PeaksAndValleys {
    public static void main(String[] args) {
        int [] numbers = {5, 3, 1, 2, 3};
        System.out.println(solution(numbers));

    }

    public static int[] solution(int[] numbers) {
        // A: init 2 pointers
        int prevNdx = 0, nextNdx = 1;
        // B: check the first pointers - init expection for 3rd 
        boolean nextShouldBeGreater = false;
        if (numbers[nextNdx] <= numbers[prevNdx]) {
            nextShouldBeGreater = true;
        }
        prevNdx += 1;
        nextNdx += 1;
        // C: make swaps as neeed
        while(nextNdx < numbers.length) {
            // D: if nextElem != meet expection --> swap,
            boolean nextIsGreater = (numbers[nextNdx] >= numbers[prevNdx]);
            if(nextIsGreater != nextShouldBeGreater) {
                int temp = numbers[prevNdx];
                numbers[prevNdx] = numbers[nextNdx];
                numbers[nextNdx] = temp;
            }
            // E: move both pointers ahead
            prevNdx += 1;
            nextNdx += 1;
            // F: alternate the expectation for the next value
            nextShouldBeGreater = !nextShouldBeGreater;
        }
        // F: return the array
        return numbers;
    }
}
