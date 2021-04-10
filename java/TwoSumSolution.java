import java.lang.Integer;
import java.util.ArrayList;
import java.util.HashMap;

class TwoSumSolution {
    /*
     * duplicates possible pos or negative unsorted at least 2 elements exactly 1
     * solution, doesn't matter what order are we allowed to sort? yes
     */
    public int[] twoSum(int[] nums, int target) {
        // map unique values to their indices
        HashMap<Integer, ArrayList<Integer>> values = new HashMap<Integer, ArrayList<Integer>>();
        for (int index = 0; index < nums.length; index += 1) {
            int element = nums[index];
            // adding a new ArrayList
            if (values.containsKey(element) == false) {
                ArrayList<Integer> indices = new ArrayList<Integer>();
                indices.add(index);
                values.put(element, indices);
            }
            // adding to previous ArrayList
            else {
                ArrayList<Integer> indices = values.get(element);
                indices.add(index);
                values.put(element, indices);
            }
        }
        // flag
        // iterate through the ArrayList until we find a differernt index - 1 or 2
        // iterations at most each time
        // find the first index
        int[] addends = new int[2];
        for (int firstIndex = 0; firstIndex < nums.length; firstIndex += 1) {
            int elem = nums[firstIndex];
            int diff = target - elem;
            // find the second index
            if (values.containsKey(diff) == true) {
                addends[0] = firstIndex;
                // find + return both indices
                ArrayList<Integer> indices = values.get(diff);
                int secondIndex = firstIndex;
                int indicesIndex = 0;
                while (indicesIndex < indices.size() && firstIndex == secondIndex) {
                    secondIndex = indices.get(indicesIndex);
                    if (firstIndex != secondIndex) {
                        addends[1] = secondIndex;
                        return addends;
                    } else {
                        indicesIndex += 1;
                    }
                }
            }
        }
        return addends;
    }
}