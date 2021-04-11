public class BitInsertion {
    /* Insertion: You are given 
     * two 32-bit numbers, N and M, and 
     * two bit positions, i and j. 
     * 
     * Write a method to insert M into N such that M starts at bit j and ends at bit i. 
     * You can assume that the bits j through i have enough space to fit all of M. 
     * That is, if M= 10011, 
     * you can assume that there are at least 5 bits between j and i. 
     * You would not, for example, have j = 3 and i = 2, 
     * because M could not fully fit between bit 3 and bit 2.
     * 
     * EXAMPLE
     * Input: N = 10_000_000_000, M = 10011, i = 2, j = 6
     *            10000000000
     *                1001100
     * Output: N = 10001001100
     *             09876543210
     * 
     * Clarifications:
     * 1) assume j >= i? yes
     * 2) indices are 0-indexed, go from greatest to least (powers of 2)
     * 3) signed or unsigned integers? ASSUME they're unsigned
     * 4) ASSUME that input is mutable
     * 
     * Intuition:
     *      3 parts of N = part before j, part between j and i, part after i
     * Approach:
     *      1. using an updateBit operation
     *          - add i trailing zeroes to M --> arthimetic right shift
     *          - do a bitwise OR on N and M, update N
     * Edge Cases:
     *      i == j --> changing a single bit (N = 100, M = 0, i = j = 2)
     *      j == first place value -- follow updateBit operation --> still work b/c we push forward the leftmost bit
     *          - N = 1011, M = 11, i = 2, j = 3
     *      i == 0 -- another updateBit operation
     *       j - i > len(M)? ---> raise an Exception
     *          M = 101010101
     *          N = 110
     *          i = 5, j = 1 --> what to do?
     *
     */

    public static int lengthOfBinaryNum(int M) {
        /* count how long it takes to make this value 0, via arithmetic left shifts */
        int count = 0;
        while (M > 0) {
            count += 1;
            M = M >> 1;
        }
        return count;
    }

    public static int solution(int N, int M, int i, int j) {
        // Time: O(log(M)), space is constant
        // A: validate j - i == length of M
        int lengthM = lengthOfBinaryNum(M);
        if ((j - i + 1) != lengthM) {
            throw new IllegalArgumentException(
                "The space between and j and i must be the length of M, " + lengthM
            );
        }
        // B: add i trailing zeroes to M --> arthimetic right shift
        M = M << i;
        // C: do a bitwise OR on N and M, update N
        N = N | M;
        return N;
    }

    public static void main(String[] args) {
        int N = 128, M = 19, i = 2, j = 6;
        System.out.println(solution(N, M, i, j));
    }
}
