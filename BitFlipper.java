/*
 * The following solution is provided for the Hacker Rank problem at this link:
 * http://hr.gs/bddefe 
 */
import java.lang.*;

public class BitFlipper {

    // Complete the flippingBits function below.
    /*
     * Pre: long n is an unsigned decimal integer
     * Post: long is an unsigned decimal integer, and is found by
     *       "flipping" all the bits in the binary representation 
     *      of the input
     */
    static long flippingBits(long n) {
        // convert n to 32-bit number
        int[] nInBinary = new int[32];
        double maxExponent = nInBinary.length - 1;
        // populate the array with 0's and 1's
        for(int i = 0; i < maxExponent + 1; i++)
        {   
            // see if a 1 can be placed here 
            double base = 2.00, exponent = maxExponent - i;
            double power = Math.pow(base, exponent);
            if(power <= n && n % power >= 0) {
                nInBinary[i] = 1;
                n -= power;
            // otherwise place a 0 in this place
            } else {
                nInBinary[i] = 0;
            }
        }
        // flip bits
        for(int i = 0; i < nInBinary.length; i++) {
            if (nInBinary[i] == 0) {
                nInBinary[i] = 1;
            } else {
                nInBinary[i] = 0;
            }
        }
        // return the equivalent of the flipped binary number
        long newNum = 0;
        for(int i = 0; i < maxExponent + 1; i++)
        {   
            // calculate the power
            double base = 2.00, exponent = maxExponent - i;
            double power = Math.pow(base, exponent);
            // 1's indicate powers of 2 to be added to newNum
            if(nInBinary[i] == 1){
                newNum += power;
            }
        }
        return newNum;
        
    }

    public static void main(String[] args) {
        
    }
}
