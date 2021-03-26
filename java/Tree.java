import java.util.ArrayList;

public class Tree {
    BinaryTreeNode root;

    public Tree(BinaryTreeNode root) {
        this.root = root;
    }

    public void bfs() {
        // A: init a queue
        ArrayList<BinaryTreeNode> q = new ArrayList<BinaryTreeNode>();
        // B: enqueue the root
        if (this.root != null) {
             q.add(this.root);
        }
        // C: traverse the tree
        while (q.size() > 0) {
            // D: dequeue a node on each iteration
            BinaryTreeNode frontNode = q.get(0);
            q.remove(0);
            // E: visit the node
            System.out.println(frontNode);
            // F: enqueue the node's children
            if (frontNode.left != null) {
                q.add(frontNode.left);
            }
            if (frontNode.right != null) {
                q.add(frontNode.right);
            }
        }
    }

    public void dfsRecursive(BinaryTreeNode node) {
        // RECURSIVE case
        if (node != null) {
            // traverse the left subtree
            if (node.left != null) {
                this.dfsRecursive(node.left);
            }
            // visit this node
            System.out.println(node);
            // traverse the right subtree
            if (node.right != null) {
                this.dfsRecursive(node.right);
            }
        }
    }

    public void dfsRecursive() {
        // BASE case
        if (this.root != null) {
            this.dfsRecursive(this.root);
        }
    }
    
    // TEST CASES
    public static void main(String[] args) {
        // A: init the tree
        BinaryTreeNode node1, node2, node3;
        node1 = new BinaryTreeNode(1);
        node2 = new BinaryTreeNode(6);
        node3 = new BinaryTreeNode(7);
        node1.left = node2;
        node1.right = node3;
        Tree myTree = new Tree(node1);

        // B: test breadth-first search and depth-first search
        myTree.bfs();
        myTree.dfsRecursive();
    }

}

public class BinaryTreeNode {
    public int key;
    public BinaryTreeNode left, right;

    public BinaryTreeNode(int keyValue) {
        this.key = keyValue;
    }

    public String toString() {
        String str = ("Visiting Node with Value: " + this.key);
        return str;
    }
}