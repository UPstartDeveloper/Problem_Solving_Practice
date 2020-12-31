/*
 * Recursive Multiply: 
 * Write a recursive function to multiply two positive integers without using the * operator. 
 * You can use addition, subtraction, and bit shifting, 
 * but you should minimize the number of those operations.
 */


class Multiply {
    public static int multiplyRecursive(int x, int y, int product) {
        // Recursive case:
        if (y > 0) {
            // add x to itself one more time
            product += x;
            // decrement the number of times left to multiply x
            y -= 1;
            return multiplyRecursive(x, y, product);
        }
        // Base case: we've finished multiplying
        return product;
    }
    
    public static int multiplyRecursive(int x, int y) {
        // Recursive case: init the product
        int product = 0;
        // start the mutliplication
        if (x > 0 && y > 0) {
            // add x to itself one more time
            product += x;
            // decrement the number of times left to multiply x
            y -= 1;
            return multiplyRecursive(x, y, product);
        } 
        // if we're multiplying by 0, then we're good to go
        return 0;
    }
}