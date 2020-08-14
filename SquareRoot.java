import java.lang.Math;

public class SquareRoot {
    // Pre: int number is a non-negative integer value
    // Post: return the integer that is closest to the square root of number.
    //       Note: this means that any decimal part of the square root is truncated.
    public static int squareRoot(int number){
        // initialize roots
        int root1 = 0, root2 = 1;
        // early exit: if the number is 0 or 1
        if (number == 0 || number == 1) {
            return number;
        }
        // iterate until the roots are in the range of possibility
        while (Math.pow(root2, 2) < number) {
            // increment the roots
            root1 += 1;
            root2 += 1;
        }
        // root is found, because Math.pow(root1, 2) <= number < Math.pow(root2, 2)
        return root1; 
    }
    
    // Pre: None
    // Post: None - ran a test input on the squareRoot method
    public static void main(String[] args){
        int number = 8;
        System.out.println(squareRoot(number));
    }
}