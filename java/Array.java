import java.util.ArrayList;
import java.lang.Integer;

public class Array {

    public int linearSearch(ArrayList<Integer> list, int target) {
        int index = 0;
        while (index < list.size()) {
            if (list.get(index) == target) {
                return index;
            }
            index += 1;
        }
        return -1;
    }

    public int binarySearchIterative(ArrayList<Integer> list, int target) {
        // ASSUMES the list is sorted
        int low = 0, hi = list.size() - 1;
        while (low <= hi) {
            // find the middle
            int midIndex = Math.floorDiv(lo + hi, 2);
            int midElem = list.get(midIndex);
            // target found
            if (target == midElem) {
                return midIndex;
            }
            // go left
            else if (target < midElem) {
                hi = midIndex - 1;
            }
            // go right
            else {
                low = midIndex + 1;
            }
        }
        // not found
        return -1;
    } 
}