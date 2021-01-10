package sorting_problems;

public class Sort {
    /* A class for sorting an array of strings. 
     * Note: when str.compareTo < 0, the
     * value should be BEFORE
     * Assumption: each String begins with an English letter
     */
    String[] lines;

    public Sort(String[] lines) {
        this.lines = lines;
    }

    public void insertionSort(){
        // A: init the index at the second element (if it's there)
        int index = 1;
        // B: insert each element into the sorting position
        while (index < this.lines.length) {
            // C: swap this string until it is greater than the one prior
            int indexGreater = index;
            String strGreater = this.lines[indexGreater];
            while (indexGreater >= 1 && strGreater.compareTo(this.lines[indexGreater - 1]) < 0) {
                // Ci: swap this string and the one prior
                String temp = this.lines[indexGreater - 1];
                this.lines[indexGreater - 1] = strGreater;
                this.lines[indexGreater] = temp;
                // Cii: move the pointers to the string back
                indexGreater -= 1;
                strGreater = this.lines[indexGreater];
            }
            // D: increment the index
            index += 1;
        }
    }
}

/* Test Input:
 *  0  1  2  3  4
 * [H, M, N, I, S]
 *           ^ 
 *        I  N
 *     I  M
 * 
 * Result:
 * [H, I, M, N, S]
 * index    |   indexGreater    |       strG    | temp
 * 1                1                   M
 * 2                2                   N
 * 3                3                   I           N
 *                  2                   I           M
 *                  1                   I
 * 4
 * 5               
 */