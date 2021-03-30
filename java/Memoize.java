import java.util.HashMap;
import java.lang.Integer;

public class Memoize {
    HashMap<Integer, Integer> cache;

    public Memoize() {
        this.cache = new HashMap<Integer, Integer>();
    }

    public static int fib(int n) {
        /* computes the nth Fib num */
        // Base Cases
        if (n == 0 || n == 1) {
            return n;
        
        } 
        // Recursive Cases
        else {
            return fib(n - 1) + fib(n - 2);
        }
    }

    public int fibMemoizedTopDown(int n) {
        if (this.cache.containsKey(n) == false) {
            int answer = fib(n);
            this.cache.put(n, answer);
        }
        // returns the nth Fib num
        return this.cache.get(n);
    }

    public int fibMemoizedBottomUp(int n) {
        // A: init array
        int[] fibNums = new int[n];
        // B: iterate from the base cases up to the nth fib number
        for(int fibIndex = 0; fibIndex < fibNums.length; fibIndex += 1) {
            // base cases
            if (fibIndex == 0 || fibIndex == 1) {
                fibNums[fibIndex] = fibIndex;
            } else {
            // recursive cases
                fibNums[fibIndex] = fibNums[fibIndex - 1] + fibNums[fibIndex - 2];
            }
        }
        // C: return the last number in the array
        return fibNums[fibNums.length - 1];
    }
}