import java.util.Deque;
import java.lang.Integer;
import java.util.Iterator;


public class MaximumLevelSum {
    public static int solution(BinaryTreeNode root) {
        // A: init output
        if (root == null) {
            throw new NullPointerException("This tree is undefined.");
        }
        // B: validate input
        else {
            int maxSum = Integer.MIN_VALUE;
            // C: init queue (for BFS)
            Deque<BinaryTreeNode> q = new Deque<BinaryTreeNode>();
            q.addLast(root);
            // D: linear search the levels for the highest level sum
            while (q.size() > 0) {
                // E: calculate the level sum here
                int levelSum = 0;
                Iterator levelIterator = q.iterator();
                while (levelIterator.hasNext()) {
                    levelSum += levelIterator.next().key;
                }
                // F: update maximum if needed
                if (levelSum > maxSum) maxSum = levelSum;
                // G: enqueue the next level
                int levelSize = q.size();
                for (int enqueueOps = 0; enqueueOps < levelSize; enqueueOps ++) {
                    BinaryTreeNode node = q.removeFirst();
                    if (node.left != null) {
                        q.addLast(node.left);
                    }
                    if (node.right != null) {
                        q.addLast(node.right);
                    }
                } 
            }
            // H: return the max
            return maxSum;
        }   
    }
}

public class BinaryTreeNode {
    int key;
    BinaryTreeNode left, right;

    public BinaryTreeNode(int key) {
        this.key = key;
    }
}