import java.util.LinkedList;
import java.lang.Math;

public class SortedListToBST {

    public static Tree convertArrayToBST(Integer[] array, Tree result) {
        // A: find the middle of the whole array
        int mid = Math.floorDiv(0 + array.length - 1, 2);
        // B: set the root of the tree
        result.root = new BinaryTreeNode(array[mid]);
        // C: set the left and right children of the root
        result.root.left = convertArrayToBST(array, 0, mid - 1);
        result.root.right = convertArrayToBST(array, mid + 1, array.length - 1);
        // D: return the tree
        return result;
    }

    public static BinaryTreeNode convertArrayToBST(Integer[] array, int low, int high) {
        // A: find the middle of this range in the array
        int mid = Math.floorDiv(low + high, 2);
        // B: set the left and children of this node
        BinaryTreeNode node = new BinaryTreeNode(array[mid]);
        node.left = convertArrayToBST(array, low, mid - 1);
        node.right = convertArrayToBST(array, mid + 1, high);
        // C: return the node
        return node;
    }

    public static Tree solution(LinkedList<Integer> nums) {
        // A: init output
        Tree result = new Tree();
        // B: validate input 
        if (nums != null) {
            // C: convert linked list to array
            Integer[] numsArray = nums.toArray(new Integer[nums.size()]);
            // D: convert array to BST
            result = convertArrayToBST(numsArray, result);
        }
        // E: output the tree
        return result;
    }
}