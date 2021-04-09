public class ProductOfArrayExceptSelf {
    public static int[] solve(int[] nums) {
        int[] output = {};
        // A: valudate input 
        if (nums.length > 0) {
            output = new int[nums.length];
            // B: populate array w/ products from left
            int product = 1;
            for (int index = 0; index < output.length; index += 1) {
                output[index] = product;
                product = product * nums[index];
            }
            // C: update array w/ products from the right
            product = 1;
            for (int index = output.length - 1; index > -1; index -= 1) {
                output[index] *= product;
                product = product * nums[index];
            }
        }
        // D: return the array
        return output;
    }
}
